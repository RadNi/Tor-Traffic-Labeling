TOR Packet Labeling 

How It Works?

The process_batch.py script tries to label every packet in pcap with its label. The script do an efficient search for finding packets related to every cell payload.
    - Inputs:
        - captured packets (which tshark recorded)
        - labeled cells (which our modified TOR client provided for us)
        - mac address of capturer machine (is needed to split packets by direction.)
    - Outputs:
        - results.out 
            - This is the final result of our labeling process. 
            - In this file, for each ssl packet which has label, the number is shown and all the labels for this packet is shown. 

Example:
    - python3.6 label_packets.py packets.py labeled_cells.out ff:ff:ff:ff:ff:ff
