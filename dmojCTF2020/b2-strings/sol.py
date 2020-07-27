#!/usr/bin/env python

from pwn import *

e = ELF('./main')

addr = 0x00007fffffffd920

for i in range(1, 100):
    io = e.process(stdout=-1, stderr=1, level='error')
    print(i, flush=True)
    io.sendline(f"A\x00" * i)