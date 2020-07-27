#!/usr/bin/env python

import base64
import string
from itertools import product
from Crypto.Cipher import AES
from rich.progress import track
enc = b'53rW_RiyUiwXq3PD7E4RHJuzjlHbw4YmG8wNRILXEQdBFiJZlpI2WjD_kNeQAUYG'
enc = base64.urlsafe_b64decode(enc)

for p in track(product(range(256), repeat=3), total=256 * 256 * 256):
    key = bytes(p) * 8
    ekey = base64.urlsafe_b64encode(key)
    cipher = AES.new(ekey, AES.MODE_ECB)
    txt = cipher.decrypt(enc)
    if b'ctf{' in txt:
        print(txt)
