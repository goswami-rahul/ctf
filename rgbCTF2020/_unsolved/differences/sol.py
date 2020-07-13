#!/usr/bin/env python
from pwn import xor
from Crypto.Util.number import *
import string

with open('DifferenceTest.java', 'rb') as f:
    a = f.read()
with open('my.java', 'rb') as f:
    b = f.read()
print(len(a), len(b))
print(a)
print(b)
ot = []
for x in a:
    if chr(x) not in string.printable:
        ot.append(chr(x))
print(''.join(ot))
exit(0)
print(a)
print(b)
c = bytes(abs(y - x) for x, y in zip(a, b))
print(c)
d = abs(int.from_bytes(a, 'little') - int.from_bytes(b, 'little'))
print(d)
print(d.to_bytes(d.bit_length() + 5, 'little'))