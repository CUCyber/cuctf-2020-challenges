from scapy.all import *

out = ""
scapy_cap = rdpcap('challenge.pcapng')
for packet in scapy_cap:
    num = 0
    try:
        flags = packet['TCP'].flags
        if 'C' in flags:
            num += 0b1000000
        if 'E' in flags:
            num += 0b100000
        if 'U' in flags:
            num += 0b10000
        if 'A' in flags:
            num += 0b1000
        if 'P' in flags:
            num += 0b100
        if 'R' in flags:
            num += 0b10
        if 'S' in flags:
            num += 0b1

        # Only account for printable ASCII values
        if ord(chr(num)) > 30:
            out += chr(num)
    except:
        pass

print(out)
