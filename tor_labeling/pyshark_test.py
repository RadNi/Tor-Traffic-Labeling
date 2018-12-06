#!/usr/bin/python3.6

import pyshark


class Cell:

    @staticmethod
    def parse_from_file_and_label(file_name):

        packets_length = len(ssl_packets)

        with open(file_name, 'r') as f:

            current_cell_line = 0
            application_name = None

            for line in f:
                cleaned_line = line.strip()

                if cleaned_line == '------------':  # a new cell has begun. 
                    current_cell_line = 0
                    continue

                if current_cell_line == 0:  # we're at the first line. should read application_name
                    application_name = cleaned_line[18:]
                    
                elif current_cell_line == 1:  # we're at the second line. should read payload.
                    payload = cleaned_line.split(' ')

                    if len(application_name) != 0: 
                        # got everything we need for the cell. time to build it. 
                        cell = Cell(application_name, payload)

                        AppData.label_packets(ssl_packets,
                                              packets_length,
                                              cell.get_payload(),
                                              cell.get_application_name())

                current_cell_line += 1

    def __init__(self, application_name, payload):
        self.application_name = application_name
        self.payload = self.__internal_check_payload(payload)

    def get_payload(self):
        return self.payload

    def get_application_name(self):
        return self.application_name

    @staticmethod
    def __internal_check_payload(payload):
        tmp_payload = ':'.join(p for p in payload).split('17:03:03:')

        if tmp_payload[0] == '' or tmp_payload[0] == '  ':
            result = ' '.join(c for c in tmp_payload[1].split(':'))
            result = result[5:]

        else:
            result = ' '.join(c for c in tmp_payload[0].split(':'))

        while result[-1] == ' ':
            result = result[:-1]

        while result[0] == ' ':
            result = result[1:]

        return ''.join(r for r in result)


class AppData:
    number = 0
    last_packet = 0

    @staticmethod
    def label_packets(packets, packets_length, payload, application_name):
        AppData.number += 1

        # starting where the last packet was found. going i packets
        # forward and backward on each iteration, hoping to find the
        # packet.
        # still thinking if packet is not found in a small distance
        # it won't be found anywhere. but for the sake of completeness,
        # needed to check them all.

        for distance in range(0, max(AppData.last_packet, packets_length - AppData.last_packet) - 1):
            forward = AppData.last_packet + distance

            if forward < packets_length:
                if payload in packets[forward].payload:
                    packets[forward].labels.add(application_name)
                    AppData.last_packet = forward
                    print(AppData.number, ' ', forward)
                    return

            backward = AppData.last_packet - distance

            if backward > -1:
                if payload in packets[backward].payload:
                    packets[backward].labels.add(application_name)
                    print(AppData.number, ' ', backward)
                    AppData.last_packet = backward
                    return

    def __init__(self, packet, number):
        self.packet = packet
        self.number = number
        self.payload = self.get_payload()
        self.labels = set()

    def get_payload(self):
        try:
            if self.packet.ssl != self.packet[-1]:
                temp = self.packet[-1].app_data
                return ' '.join(p for p in (self.packet.ssl.app_data + temp).split(':'))
            else:
                return ' '.join(p for p in self.packet.ssl.app_data.split(':'))
        except:
            return ' '.join(p for p in self.packet.ssl.app_data.split(':'))


class CapReader:
    def __init__(self, file_name):
        self.packets = pyshark.FileCapture(file_name)

    def get_all_packets(self):
        return self.packets

    def get_ssl_app_data_packets(self):
        result = []
        i = 1
        for p in self.packets:
            try:
                if p.ssl.app_data:
                    a = AppData(p, i)
                    result.append(a)
            except:
                pass
            i += 1

        return result


cr = CapReader('hello.pcap')

ssl_packets = cr.get_ssl_app_data_packets()
print("found " + str(len(ssl_packets)) + " ssl_packets")

Cell.parse_from_file_and_label('/tmp/lables_cell.out')

fw = open('./result.out', 'a+')
for ssl in ssl_packets:
    fw.write('number: ' + str(ssl.number) + '\n\t labels: ')
    for l in ssl.labels:
        fw.write(l + ' ')
    fw.write('\n')
