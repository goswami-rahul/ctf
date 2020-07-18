#!/usr/bin/env python

from pwn import *

HOST = 'insanity1.chujowyc.tf'
PORT = 4004
context.log_level = 'error'

p = remote(HOST, PORT)
p.recvuntil(b'2:')
p.sendline(b'4')
p.recvline()
p.sendline(b'81')
print(p.recvline())
p.sendline(b'42123')
flag = re.search('chCTF{.*}', p.recvline().decode())[0]
print(flag)
