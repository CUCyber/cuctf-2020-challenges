#I've hidden my data using XOR with a single byte. Don't forget to decode from base64 first.
import binascii
import base64

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

base64_encoded_text = "UkRSRVdqZ3RjaDx2fn51PGZ4ZXk8d2R/dXB8dH9lcH1ibA=="
ciphertext = (base64.b64decode(base64_encoded_text))

for i in range(255):
    candidate_key =  bytes([i])
    keystream = candidate_key * len(ciphertext)
    result = byte_xor(ciphertext, keystream)
    try:
        print(result.decode())
    except:
        print("Not decode-able")
