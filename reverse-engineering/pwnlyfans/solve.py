from z3 import *

s = Solver()

coupon = [BitVec(f"coupon_{i}", 8) for i in range(0, 23)]

s.add(coupon[14]+coupon[22] == 228)
s.add(coupon[5]+coupon[13]+coupon[16]+coupon[19]+coupon[14]+coupon[9] == 605)
s.add(coupon[18]+coupon[7]+coupon[17]+coupon[21]+coupon[2]+coupon[20] == 458)
s.add(coupon[20]+coupon[20]+coupon[2]+coupon[16]+coupon[3]+coupon[11] == 507)
s.add(coupon[12]+coupon[11]+coupon[15] == 250)
s.add(coupon[20]+coupon[8]+coupon[15]+coupon[19]+coupon[4]+coupon[12]+coupon[13] == 655)
s.add(coupon[1]+coupon[10]+coupon[16]+coupon[17]+coupon[9]+coupon[11]+coupon[4] == 564)
s.add(coupon[22]+coupon[9]+coupon[13]+coupon[15] == 439)
s.add(coupon[9]+coupon[3]+coupon[20]+coupon[11]+coupon[0] == 465)
s.add(coupon[8]+coupon[13]+coupon[8]+coupon[9]+coupon[18]+coupon[18] == 523)
s.add(coupon[15]+coupon[11]+coupon[9]+coupon[18]+coupon[5]+coupon[20]+coupon[18] == 606)
s.add(coupon[1]+coupon[20]+coupon[5]+coupon[3]+coupon[4]+coupon[8] == 579)
s.add(coupon[3]+coupon[11]+coupon[10]+coupon[15]+coupon[6] == 496)
s.add(coupon[14]+coupon[11]+coupon[0]+coupon[0]+coupon[22]+coupon[5]+coupon[0] == 655)
s.add(coupon[21]+coupon[8]+coupon[0]+coupon[15] == 379)
s.add(coupon[16]+coupon[12]+coupon[17]+coupon[16] == 203)
s.add(coupon[15]+coupon[3]+coupon[13]+coupon[15] == 384)
s.add(coupon[7]+coupon[0]+coupon[4]+coupon[2]+coupon[16] == 350)
s.add(coupon[4]+coupon[18]+coupon[11]+coupon[6] == 329)
s.add(coupon[21]+coupon[3]+coupon[6]+coupon[12]+coupon[16]+coupon[2] == 473)
s.add(coupon[4]+coupon[3]+coupon[6]+coupon[10]+coupon[22]+coupon[3]+coupon[12] == 629)
s.add(coupon[1]+coupon[16]+coupon[12]+coupon[21]+coupon[2]+coupon[2] == 422)
s.add(coupon[22]+coupon[19]+coupon[14] == 339)

s.check()
m = s.model()
b = "".join(chr(m.eval(coupon[y]).as_long()) for y in range(23)).encode('UTF-8')
print(b)
