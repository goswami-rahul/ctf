#!/usr/bin/env python
with open('hm.png', 'rb') as f:
    a = f.read()
with open('hmmmm.png', 'rb') as f:
    b = f.read()

# print(len(a))
# print(len(b))

A = []
B = []
for i in range(len(a)):
    if a[i] != b[i]:
        A.append(a[i])
        B.append(b[i])
A = bytes(A)
B = bytes(B)
# print(A)
print(B.decode())