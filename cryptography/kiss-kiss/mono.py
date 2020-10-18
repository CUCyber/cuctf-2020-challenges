import base64

#wrap ciphertext in base64
def wrapper(c):
    message_bytes = c.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message




with open("plaintext.txt") as file:
    text = file.read().strip()

with open("garbage_plaintext.txt") as file:
    garb_text = file.read().strip()



key = { }
key['a'] = 't'
key['b'] = 'u'
key['c'] = 'o'
key['d'] = 'r'
key['e'] = '&'
key['f'] = 'a'
key['g'] = 'l'
key['h'] = 's'
key['i'] = '9'
key['j'] = 'c'
key['k'] = 'd'
key['l'] = '!'
key['m'] = '_'
key['n'] = 'g'
key['o'] = 'h'
key['p'] = '1'
key['q'] = 'm'
key['r'] = 'n'
key['s'] = 'p'
key['t'] = '['
key['u'] = '*'
key['v'] = 'w'
key['w'] = 'x'
key['x'] = 'y'
key['y'] = 'z'
key['z'] = 'j'


ciphertext = ""
for char in text:
    if (char in key.keys()):
        ciphertext = ciphertext + key[char]
    else:
        ciphertext = ciphertext + char

garb_ciphertext = ""
for char in garb_text:
    if (char in key.keys()):
        garb_ciphertext = garb_ciphertext + key[char]
    else:
        garb_ciphertext = garb_ciphertext + char

#wrapper
base64_message = wrapper(ciphertext)
base64_garbage = wrapper(garb_ciphertext)

print(base64_message)
print("\n\n")
print(base64_garbage)
# print(base64.b64decode(base64_message))
# print(ciphertext)
with open("message.txt", 'w') as file:
    file.write(base64_message)

with open("garbage.txt", "w") as file:
    file.write(base64_garbage)
