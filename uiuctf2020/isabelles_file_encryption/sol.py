#!/usr/bin/env python
import re

with open('blackmail_encrypted', 'rb') as f:
    enc = f.read()

def super_secret_decryption(ciphertext, password):
    remove_spice = lambda b: 0xff & ((b >> 1) | (b << 7))
    plaintext = bytearray(remove_spice(c ^ password[i % len(password)]) for i, c in enumerate(ciphertext))
    return plaintext

for i in range(0, len(enc) - 7):
    add_spice = lambda b: 0xff & ((b << 1) | (b >> 7))
    pswd = bytearray(add_spice(c) ^ d for c, d in zip(b'Isabelle', enc[i:]))
    pswd = pswd[-i%8:] + pswd[:-i%8]
    try:
        if pswd.decode().isalpha():
            flag = super_secret_decryption(enc, pswd).decode()
            m = re.search('uiuctf{.*}', flag)
            if m:
                print(m[0])
                with open('dec.txt', 'w') as f:
                    f.write(flag)
                break
    except UnicodeDecodeError:
        pass