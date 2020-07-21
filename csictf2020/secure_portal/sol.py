#!/usr/bin/env python

a = ["2-4", "substring", "4-7", "getItem", "deleteItem", "12-14", "0-2", "setItem", "9-12", "^7M", "updateItem", "bb=", "7-9", "14-16", "localStorage"]

with open('obf.js', 'r') as f:
    s = f.read()

for i in range(len(a)):
    s = s.replace(f'a("{hex(i)}")', f'"{a[i]}"')

easing = ["localStorage", "getItem", "setItem", "deleteItem", "updateItem"]

for i in range(len(easing)):
    s = s.replace(f'easing[{i}]', f'"{easing[i]}"')
with open('ez.js', 'w') as f:
    f.write(s)

rules = [("9-12", "BE*"),("4-7", "bb="),("0-2", "5W"),("16", "^7M"),("12-14", "pg"),("7-9", "+n"),("14-16", "4t"),("2-4", "$F")]
pwd = ['_'] * 17

for rng, pat in rules:
    rng = list(map(int, rng.split('-')))
    if len(rng) == 1:
        pwd[rng[0]:] = list(pat)
    else:
        i, j = rng
        pwd[i:j] = list(pat)

pwd = ''.join(pwd)
print(pwd)