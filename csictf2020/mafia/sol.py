#!/usr/bin/env python

from pwn import *

HOST = 'chall.csivit.com'
PORT = 30721

N = 300
H = 1000000

io = remote(HOST, PORT)

a = list(range(1, N + 1))
random.shuffle(a)

best = 1
cnt = 0

with log.progress('Interacting') as p:
    for at, i in enumerate(a):
        p.status(f"Asking {at}: {cnt} {best}")
        cnt += 1
        io.sendline(f'1 {i} {best}')
        res = io.recvline().decode().strip()
        if res == 'G':
            lo, hi = best, H
            while lo < hi:
                md = (lo + hi + 1) >> 1
                cnt += 1
                io.sendline(f'1 {i} {md}')
                res = io.recvline().decode().strip()
                if res == 'L':
                    hi = md - 1
                else:
                    lo = md
            best = max(best, lo)

log.info(f'cnt = {cnt}')
io.sendline(f'2 {best}')
print(re.search('csictf{.*}', io.recvline().decode())[0])