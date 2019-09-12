import sys

file_path = sys.argv[1]

def read_label_from_file(fd):
    label = b""
    while True:
        byte = fd.read(1)
        if byte == b' ':
            return label.decode('ascii')
        if byte == b'':
            return None
        label += byte


def read_payload_from_file(fd):
    payload = b''
    for i in range(509):
        payload += fd.read(1)
    fd.read(1)
    return payload


def file_reader():
    with open(file_path, "rb") as fd:
        while True:
            label = read_label_from_file(fd)
            if not label:
                break
            payload = read_payload_from_file(fd)
            yield (label, payload)


for label, payload in file_reader():
    print(label, payload)
