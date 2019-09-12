#!/usr/bin/python3.6


import pyshark
import sys

packets_file = sys.argv[1]
labeled_cells_file = sys.argv[2]

# capturer system mac address
eth_dst = sys.argv[3]

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
        if application_name == "http":
            self.application_name = "apt-get"
        else:
            self.application_name = application_name
        self.payload = self.__internal_check_payload(payload)

    def get_payload(self):
        return self.payload

    def get_application_name(self):
        return self.application_name

    @staticmethod
    def __internal_check_payload(payload):
        return ':'.join(payload)


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
                    # print(packets[forward].number, AppData.number , 'label :', application_name)
                    AppData.last_packet = forward
                    # AppData.MaxDistance = 100
                    return
                elif forward + 1 < packets_length:
                    if payload not in packets[forward+1].payload:
                        if payload in packets[forward].payload + ":" + packets[forward+1].payload:
                            packets[forward].labels.add(application_name)
                            packets[forward+1].labels.add(application_name)
                            AppData.last_packet = forward + 1;
                            # print(packets[forward].number, packets[forward + 1].number, AppData.number, 'label :', application_name)
                            return
                        # if len(packets[forward].payload + packets[forward+1].payload) < len(payload):
                            # print("bad", packets[forward].number, packets[forward+1].number, len(packets[forward].payload + packets[forward+1].payload))
                            #import os
                            #os.system("echo " + payload + " >> ./shit.out")
                            #os.system("echo " + "---------------------" + " >> ./shit.out")

            backward = AppData.last_packet - distance

            if backward > -1:
                if payload in packets[backward].payload:
                    packets[backward].labels.add(application_name)
                    # print(packets[backward].number, AppData.number , 'label :', application_name, "in backward search which is improbable")
                    AppData.last_packet = backward
                    # AppData.MaxDistance = 100
                    return

        # print("cell not found", AppData.number)

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
                if p.tcp.payload and p.eth.dst == eth_dst:
                    a = AppData(p, i)
                    result.append(a)
            except:
                pass
            i += 1
        return result
    


def get_label_for_batch(packet_batch):
    counts = {}
    for ssl_packet in packet_batch:
        for label in ssl_packet.labels:
            if label in counts:
                counts[label] += 1
            else:
                counts[label] = 1

    max_count = 0
    max_label = "Unknown"

    threshold = Label_Batch_Size * Label_Batch_Threshold

    for label in counts:
        if counts[label] > max_count and counts[label] > threshold:
            max_count = counts[label]
            max_label = label

    return max_label



def batch(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]





# read the pcap and write the relevant ones in the sanitized folder

cr = CapReader(packets_file)
ssl_packets = cr.get_ssl_app_data_packets()

print("found " + str(len(ssl_packets)) + " ssl_packets")






# label the packets

Cell.parse_from_file_and_label(labeled_cells_file)




# output the result in santized folder

print("total cells : ", AppData.number)
print("duplicate cells : ", Cell.duplicate_cells)
print("very small cells : ", Cell.very_small_cells)

fw = open('result.out', 'w')
fw.write('Each line contains packet number in pcap and its labels.')
for ssl in ssl_packets:
    if not ssl.labels:
        continue
    fw.write(str(ssl.number))
    for l in ssl.labels:
        fw.write(' ' + l)
    fw.write('\n')

print("Results writed into result.out file.")
