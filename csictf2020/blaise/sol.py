#!/usr/bin/env python
from pwn import *
from math import factorial

HOST = 'chall.csivit.com' 
PORT = 30808

context.log_level = 'error'

# e = ELF('./blaise')
# io = e.process()
io = remote(HOST, PORT)

n = int(io.recvline().decode())
for i in range(n + 1):
    io.sendline(str(factorial(n) // factorial(i) // factorial(n - i)))
m = re.search(b'csictf{.*}', io.recv()) 
print(m[0].decode())