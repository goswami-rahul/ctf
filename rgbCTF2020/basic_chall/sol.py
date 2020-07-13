#!/usr/bin/env python
from base64 import b64decode
with open('basic_chall.txt') as f:
    a = f.read().strip().split()

a = [int(x, 2) for x in a]
a = ''.join(chr(x) for x in a).split()

a = [int(x, 16) for x in a]
a = ''.join(chr(x) for x in a)

a = b64decode(a).decode().split()

a = [int(x, 8) for x in a]
a = ''.join(chr(x) for x in a)

print(a)