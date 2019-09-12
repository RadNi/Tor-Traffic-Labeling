# Labeling traffic inside Tor anonymity network

## Getting Started

In this fork of torproject our goal is to lable traffic inside tor.
after labeling tor traffic we want to impelement a specefic neural network
for learning application by application traffic inside Tor network.

### Installing

To build Tor from a just-cloned git repository:

```
  sh autogen.sh && ./configure && make && make install
```
For using onion skin labeler feature:

```
  sh autogen.sh && ./configure CFLAGS='-DCAPTURE_SKINS' && make && make install
```

## Runing

In this version labeling mechanism only support socks5 tunneling.

Befor starting Tor listener you should capture packets arriving with tshark.


First start tor listener with sudoer previlage.

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

In ```labeling_process``` directory two labeling method implemented.

## Issues

This version of Tor-Traffic-Labeling needs modified OpenSSL to use SSL_read_tor api. The modified library will be published soon.
Now only we can label inbound traffic. For outbound buffers we have problem for finding the exact bytes is writing in socket
after SSL encryption.


