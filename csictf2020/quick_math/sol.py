#!/usr/bin/env python

# from sympy.ntheory.modular import crt
# from sympy import factorint
# from math import gcd
# from factordb.factordb import FactorDB
from Crypto.Util.number import *

n = [86812553978993, 81744303091421, 83695120256591]
c = [8875674977048, 70744354709710, 29146719498409]

for pw in range(10000000):
    d = [inverse(pw, p - 1) for p in n]
    m = [pow(ci, di, ni) for ci, di, ni in zip(c, d, n)]
    if len(set(m)) == 1:
        print(pw, m)
        for i in range(3):
            print(hex(m[i]))
# k, m = crt(n, c)

# for i in range(1):
#     t = k + i * m
#     f = factorint(t)
#     # fac = FactorDB(t)
#     # fac.connect()
#     # f = fac.get_factor_from_api()
#     # f = {int(p): c for p, c in f}
#     print(f)
#     # break
#     g = 0
#     for v in f.values():
#         g = gcd(g, v)
#     # print(i, t, g)
#     flag = 1
#     for p in f:
#         f[p] //= g
#         flag *= pow(p, f[p])
#     print(flag)
#     for j in range(10000000000):
#         u = flag + j * m
#         # print(u)
#         try:
#             print(u, u.to_bytes(200, 'big').decode())
#         except UnicodeDecodeError:
#             pass
#     break

# for i in range(3):
#     assert pow(flag, 3, n[i]) == c[i]
# print(g, f)
# print(f'csictf{{{flag}}}')