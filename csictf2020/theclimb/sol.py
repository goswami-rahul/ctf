#!/usr/bin/env python

import numpy as np

key = 'gybnqkurp'
enc = 'lrzlhhombgichae'


a = [8, 5, 10, 21, 8, 21, 21, 12, 8]
a = np.array(a)
a = np.reshape(a, (3, 3))

flag = []
for i in range(0, len(enc), 3):
    b = np.array([ord(c) - ord('a') for c in enc[i:i+3]])
    flag += [chr(c % 26 + 97) for c in np.matmul(a, b)]

print(''.join(flag))