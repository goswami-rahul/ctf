#!/usr/bin/env python

from pwn import *
from math import gcd, factorial

HOST = 'chall.csivit.com'
PORT = 30827

context.log_level = 'error'

io = remote(HOST, PORT)
# io = process('./RickNMorty', level='debug')

while True:
    s = io.recvline()
    if s.startswith(b'fun'):
        break
    x, y = map(int, s.decode().split())
    io.sendline(str(factorial(gcd(x, y) + 3)))

io.recvline()
print(io.recvline().decode().strip())