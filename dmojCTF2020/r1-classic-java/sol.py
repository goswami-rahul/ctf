#!/usr/bin/env python
from itertools import product
def f(s):
    if not s:
        return s
    k = len(s)
    return s[k//5:] + s[:k//2] + f(s[:k//2])

a = list(range(10))
b = f(a)
d = len(b)

e = '18 29 14 27 11 86 87 87 99 23 18 29 14 23 18 29 14 99 23 99 23 99 99 45 23 6 22 7 1 26 31 100 59 45 23 6 59 45 23 6 100 59 100 59 100 100 29 23 13 27 19 57 58 101 94 89 29 23 13 89 29 23 13 94 89 94 89 94 94 81 87 7 60 44 115 31 81 87 31 81 87 31 31'
e = bytes(map(int, e.split()))
t, r = divmod(len(e), d)

m = {}
for i in range(1, 11):
    m[len(f(a[:i]))] = i

c = []
for i in range(0, len(e), d):
    c.append(e[i:i+d])

for i in range(len(c)):
    k = len(c[i])
    k = m[k]
    a = list(range(k))
    b = f(a)
    assert(len(b) == len(c[i]))
    idx = [-1] * k
    for j, v in enumerate(b):
        idx[v] = j
    c[i] = bytes(c[i][idx[j]] for j in range(k))

def two(w):
    if not w:
        return w
    w[:-1] = two(w[:-1])
    for i in range(0, len(w) - 1):
        w[i] ^= w[-1]
    return [w[-1]] + w[:-1]

def one(w):
    for j in range(1, len(w)):
        w[j] ^= w[j - 1]
    return w

for op in product([0, 1], repeat=len(c)):
    flag = []
    for i in range(len(c)):
        cur = list(c[i])
        if op[i]:
            cur = one(cur)
        else:
            cur = two(cur)
        flag.extend(cur)
    flag = bytes(flag)
    try:
        flag = flag.decode('ascii')
        if 'ctf{' in flag:
            print(flag)
    except UnicodeDecodeError:
        pass