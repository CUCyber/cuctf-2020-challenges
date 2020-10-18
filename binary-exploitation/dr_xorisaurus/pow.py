#!/usr/bin/env python3

import hashlib
import random
import os

if __name__ == '__main__':
    goal = hex(random.randint(0x100000, 0xFFFFFF))[2:]
    proof = input("Find Sha256 starting with %s: " % goal)
    result = hashlib.sha256(proof.encode()).hexdigest()

    if result[:len(goal)] == goal:
        print('proof of work success... starting binary\n')
        os.system('./dr_xorisaurus')
    else:
        print('proof of work failed... no bruteforcing for you!')