#!/usr/bin/env python

pat = "9|2/9/:|4/7|8|4/2/1/2/9/"
flag = []
for i in range(0, len(pat), 2):
    flag.append(chr(2 * ord(pat[i]) + (pat[i + 1] == '/')))
flag = ''.join(flag)
print(f'rgbCTF{{{flag}}}')