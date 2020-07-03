#!/usr/bin/env python

with open('hex.txt', 'r') as f:
    a = f.readline().strip()
    a = a.replace('o', '0')
a = bytes([int(a[i:i + 2], 16) for i in range(0, len(a), 2)]).decode('utf8')
a.strip()
a = a.replace('V', '_')  # 56 => 5f
a = a.replace('Y', '_')  # 59 => 5f
a = a.replace('`eant', 'meant')  # 6c => 6d
a = a.replace('rea`ize', 'realize')  # 6c => 60
print('CSCML2020{' + a)