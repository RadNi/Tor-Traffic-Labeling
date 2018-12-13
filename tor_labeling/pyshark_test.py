#!/usr/bin/python3.6

import pyshark


class Cell:
    duplicate_cells = 0
    very_small_cells = 0

    @staticmethod
    def parse_from_file_and_label(file_name):

        packets_length = len(ssl_packets)
        i = 0
        with open(file_name, 'r') as f:
            i += 1
            current_cell_line = 0
            application_name = None
            last_cell = None

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

                        # check if it's the same as the last cell.
                        if last_cell:
                            if last_cell.application_name == cell.application_name and last_cell.payload == cell.payload:
                                Cell.duplicate_cells += 1
                                continue
                        last_cell = cell

                        # print("cell ", AppData.number, ":", cell.payload[:60])

                        # check if payload length is longer than a certain limit.
                        if len(cell.payload) < 100:
                            Cell.very_small_cells += 1
                            continue

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

        if len(tmp_payload) > 1:
            result = tmp_payload[1]
            result = result[6:]
        else:
            result = tmp_payload[0]

        while len(result) > 0 and result[-1] == ' ':
            result = result[:-1]

        while len(result) > 0 and result[0] == ' ':
            result = result[1:]

        return result


class AppData:
    number = 0
    last_packet = 0
    MaxDistance = 1000

    # hash_map = {}

    @staticmethod
    def label_packets(packets, packets_length, payload, application_name):
        AppData.number += 1

        # starting where the last packet was found. going i packets
        # forward and backward on each iteration, hoping to find the
        # packet.
        # still thinking if packet is not found in a small distance
        # it won't be found anywhere. need a way to implement this.

        dist_to_end = max(AppData.last_packet, packets_length - AppData.last_packet - 1)

        for distance in range(0, min(dist_to_end, AppData.MaxDistance)):
            forward = AppData.last_packet + distance

            if forward < packets_length:
                if payload in packets[forward].payload:
                    packets[forward].labels.add(application_name)
                    print(AppData.number, ' ', forward, ' label : ', application_name)
                    AppData.last_packet = forward
                    # AppData.MaxDistance = 100
                    return
            backward = AppData.last_packet - distance

            if backward > -1:
                if payload in packets[backward].payload:
                    packets[backward].labels.add(application_name)
                    print(AppData.number, ' ', backward, ' label : ', application_name)
                    AppData.last_packet = backward
                    # AppData.MaxDistance = 100
                    return

        # AppData.MaxDistance = int(AppData.MaxDistance * (packets_length ** (1/800)))
        # print("*", end="")

    def __init__(self, packet, number):
        self.packet = packet
        self.number = number
        self.payload = self.get_payload()
        self.labels = set()

    def get_payload(self):
        return self.packet.tcp.payload


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


cr = CapReader('packets.pcap')

ssl_packets = cr.get_ssl_app_data_packets()
print("found " + str(len(ssl_packets)) + " ssl_packets")

# cell_size = 543
# i = 0
# for packet in ssl_packets:
#     l = len(packet.payload)
#     if l < cell_size:
#         m = md5.new()
#         m.update(packet.payload)
#         AppData.hash_map[m.digest()] = i
#     else :
#         for j in range(0, l - cell_size + 1):
#             m = md5.new()
#             m.update(packet.payload[j:j + cell_size])
#             AppData.hash_map[m.digest()] = i
#     i += 1

Cell.parse_from_file_and_label('lables_cell.out')

print("total cells : ", AppData.number)
print("duplicate cells : ", Cell.duplicate_cells)
print("very small cells : ", Cell.very_small_cells)

fw = open('./result.out', 'w+')
for ssl in ssl_packets:
    fw.write('number: ' + str(ssl.number) + '\n\t labels: ')
    for l in ssl.labels:
        fw.write(l + ' ')
    fw.write('\n')
