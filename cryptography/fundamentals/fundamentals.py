import base64

FLAG = "CUCTF{very-good-with-fundamentals}"

XORED_FLAG = ""
KEY = 0x11
for char in FLAG:
    XORED_FLAG += chr(ord(char) ^ KEY)

BASE64_FLAG = base64.b64encode(XORED_FLAG.encode())
print(BASE64_FLAG.decode())