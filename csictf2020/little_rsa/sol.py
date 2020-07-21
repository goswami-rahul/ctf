#!/usr/bin/env python

c = 32949
n = 64741
e = 42667

for m in range(n):
    if c == pow(m, e, n):
        print(m)