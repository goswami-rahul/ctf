#!/usr/bin/env python

a = b'|A4$wb!Of(O6H>5PQ?6Tb&CJEHELIK?6a~BP?'
a = a[::-1]  # reverse
b = []
for i in range(len(a)):
    c = a[i]
    q = ' '
    if c <= ord('i') - ord('0') and c >= ord('i') - ord('9'):
        d = ord('i') - c
    if ord('a') <= c + 36 and c + 36 <= ord('z'):
        d = c + 36
    if ord('A') <= c - 29 and c - 29 <= ord('Z'):
        d = c - 29
    if ord('~') == c:
        d = ord('{')
    if ord('|') == c:
        d = ord('}')
    if ord('!') + i % 10 == c:
        d = ord('_')
    
    b.append(chr(d))

print(''.join(b))