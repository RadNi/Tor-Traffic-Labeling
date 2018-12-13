#!/bin/bash

i=1;
while [ $i -lt 20 ]
do
    rm /tmp/lables_cell.out
    fuser -k 9050/tcp

    NAME=`date "+%Y-%m-%d-%H-%M-%S"`;
    mkdir $NAME;
    cp pyshark_test.py $NAME;
    cd $NAME;

    tor &
    tcpdump -i wlp8s0 -s 65535 -w packets.pcap &
    sleep 10;
    ./../bot.sh &



    sleep 150;



    fuser -k 9050/tcp;
    sleep 5;
    killall tcpdump;

    cp /tmp/lables_cell.out ./;
    python3.6 pyshark_test.py &
    cd .. ;

i=$[$i+1]

done





