#!/usr/bin/env python3

import gmpy2
from Crypto.Util.number import getPrime, bytes_to_long

FLAG = ?

def gen_next_prime(p):
    q = p
    for i in range(20000):
        q = gmpy2.next_prime(q)
    return q

p = getPrime(1024)
q = gen_next_prime(p)
m = bytes_to_long(FLAG)
n = p * q
e = 0x10001
c = pow(m,e,n)

print(f"n = {n}")
print(f"e = {e}")
print(f"c = {c}")
