#!/usr/bin/env python
from sympy import mod_inverse, primefactors

n = 5620911691885906751399467870749963159674169260381
e = 65537
c = 1415060907955076984980255543080831671725408472748

p, q = primefactors(n)
phi = (p - 1) * (q - 1)
d = mod_inverse(e, phi)
flag = pow(c, d, n)
print(flag.to_bytes(flag.bit_length(), 'little').decode())