# Brute force 2 bytes into CTR bit flipping attack
import requests

url = "http://127.0.0.1:7500"

# need to bf two bytes
base = "CUCTF{"

def bf():
    for i in range(0x40,0x7f):
        for j in range(0x40,0x7f):
            curr = base + chr(i) + chr(j)
            data = {'author':'admim', 'note':curr}

            r = requests.post(url+'/register', data=data)
            cookie = r.text
            r = requests.get(url+'/read/'+cookie)
            if "going on" in r.text:
                print("FOUND: " + curr)
                return cookie

cookie = bf()
new_cookie = cookie[:-6] + hex((int(cookie[-6:-4],16)^37)^38)[2:] + cookie[-4:]
r = requests.get(url+"/read/"+new_cookie)
print(r.text)
