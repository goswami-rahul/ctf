#!/usr/bin/env python
from pwn import *
from random import seed, randint as w
from time import time

context.log_level = 'error'

HOST = 'challenge.rgbsec.xyz'
PORT = 12345

io = remote(HOST, PORT)
t = int(time()) - 5

io.recvline()
nums = [int(io.recvline(keepends=False)) for _ in range(10)]
log.info(f"{nums}")
io.recvuntil(": ")
n = int(io.recvline(keepends=False))
log.info(f"{n}")

with log.progress("Trying seeds") as p:
    while True:
        p.status(f"Try {t}")
        seed(t)
        if nums == [w(5, 10000) for _ in range(10)]:
            break
        t += 1
    p.success(f'Found {t}')
b = bytearray([w(0, 255) for _ in range(40)])
g = bytearray([l ^ p for l, p in zip(n.to_bytes(40, 'little'), b)])
flag = []
for c in g:
    flag.append(chr(c))
    if flag[-1] == '}':
        break
flag = ''.join(flag)
print(flag)