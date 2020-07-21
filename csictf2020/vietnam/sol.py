#!/usr/bin/env python
from pwn import *
from math import factorial

HOST = 'chall.csivit.com' 
PORT = 30814

context.log_level = 'error'

# e = ELF('./vietnam')
# io = e.process()
io = remote(HOST, PORT)

lim = 0x400
stack = [0]
need = "HELLO\n"
ans = []

for char in need:
    x = ord(char)
    if stack[-1] > x:
        ans.append('$')
        stack.append(1)
    while stack[-1] < x:
        ans.append('$')
        ans.append('+')
        stack[-1] += 1
    ans.append('.')
ans = ''.join(ans)
assert len(ans) < lim

io.sendline(ans)
m = re.search(b'csictf{.*}', io.recvuntil('}')) 
print(m[0].decode())