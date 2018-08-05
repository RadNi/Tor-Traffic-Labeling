# Labeling traffic inside Tor anonimity network

## Getting Started

In this fork of torproject our goal is to lable traffic inside tor.
after labeling tor traffic we want to impelement a specefic neural network
for learning application by application traffic inside Tor network.

### Installing

To build Tor from a just-cloned git repository:

```
  sh autogen.sh && ./configure && make && make install
```

## Runing

In this version labeling mechanism only support socks5 tunneling.

Befor starting Tor listener you should capture packets arriving with tcpdump or wireshark.


First start tor listener with sudoer previlage, because of ``` -a ``` flag in netstat command used in src/or/process.h file 
for finding application name now using tor:

```
  sudo tor
```

One of the simple way using tor you can start any application with command below

```
  torify <application-name>
```

or

```
  torsocks <application-name>
```

## Labeling

the python script in ```tor_labeling``` directory will give ```.pcap``` file from tcpdump and ```/tmp/lables_cell.out``` and 
write the packet lalels in ordering of ```.pcap``` file.

## Issues

Now only we can label inbound traffic. For outbound buffers we have problem for finding the exact bytes is writing in socket
after SSL encryption.


