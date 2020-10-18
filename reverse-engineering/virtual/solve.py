import binascii
flag = "CUCTF{v1rtual_eyez_v1rtual1ze_v1rtu4l_li3ss!!!}"
enc = b""

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1)+fib(n-2)

for i in range(47):
    if i % 2 == 0:
        enc += bytes([(ord(flag[i])^8) - 15])
    else:
        tmp = (ord(flag[i])^27) + fib(i%10)
        enc += bytes([tmp])

print(binascii.b2a_hex(enc))
