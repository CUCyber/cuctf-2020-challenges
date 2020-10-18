#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Util import Counter
from flask import Flask,request
from flag import KEY, FLAG, NOTES
import hashlib
import json
import os

notes = NOTES

chal = Flask(__name__)

def encrypt(plaintext):
    iv = os.urandom(16)
    cipher = AES.new(KEY, AES.MODE_CTR, counter=Counter.new(128, initial_value=int.from_bytes(iv, 'big')))
    ciphertext = cipher.encrypt(plaintext)
    return (iv+ciphertext).hex()

def decrypt(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)
    iv = int.from_bytes(ciphertext[:16], 'big')
    cipher = AES.new(KEY, AES.MODE_CTR, counter=Counter.new(128, initial_value=iv))
    return cipher.decrypt(ciphertext[16:])

@chal.route('/register', methods=['POST'])
def register():
    try:
        note = request.form["note"]
        author = request.form["author"]
    except:
        return "Missing post data..."
    m = hashlib.md5()
    m.update(note[:8].encode())
    nid = m.hexdigest()[:8]
    if author == "admin":
        return "Cannot set author to admin!"
    cookie = f'{{"id":"{nid}","note":"{note}","author":"{author}"}}'.encode()
    return encrypt(cookie)

@chal.route('/read/<cookie>', methods=['GET'])
def read_note(cookie):
    try:
        note = json.loads(decrypt(cookie).decode())
    except Exception as e:
        return "failed :("
    for n in notes:
        if n['id'] == note['id']:
            if n['author'] == note['author']:
                return f"Note already exists...\nauthor: {n['author']}\nid: {n['id']}\nnote: {n['note']}"
            else:
                return "Different author??? What's going on here..."
    return f"author: {note['author']}\nid: {note['id']}\nnote: {note['note']}"

if __name__ == "__main__":
    chal.run(host="0.0.0.0",port=7500,threaded=True)
