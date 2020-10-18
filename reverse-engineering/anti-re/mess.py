#!/usr/bin/env python3
from sys import argv

with open(argv[1], "rb") as f:
    bindata = bytearray(f.read())

# Yes I know this is similar to `StrangerHeaders` from last year this has different results though
bindata[4] = 0x01

with open(argv[2], "wb") as f:
    f.write(bindata)
