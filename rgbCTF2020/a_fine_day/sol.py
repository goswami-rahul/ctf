#!/usr/bin/env python

txt = """
Sujd jd bgxopksbm ljsu tg tqqjgb xjkubo. Tqqjgb xjkubod tob t qvor vq dhidsjshsjvg xjkubo. 
Jsd nbp xvgdjdsd vq slv ghribod, t tgm i. 
Sv bgxopks t cbssbo, rhcsjkcp jsd kctxb jg sub tckutibs (dv t=0, i=1, bsx.) ip t, tgm subg tmm i. 
Qjgtccp stnb suts rvm 26 tgm xvgwbos js itxn jgsv t xutotxsbo.
Sub tqqjgb xjkubo jdg's obtccp suts dsovgf. 
Djgxb js'd rvm 26, subob tob vgcp t qbl uhgmobm mjqqbobgs nbpd, lujxu xtg ib btdjcp iohsb qvoxbm. Tgpltp, ubob'd pvho qctf: ofiXSQ{t_qjgb_tqqjgb_xjkubo}
"""
m = """
s - t
u - h
j - i
q - f
x - c
o - r
f - g
i - b
d - s
l - w
g - n
b - e
k - p
t - a
c - l
p - y
v - o
h - u
m - d
r - m
n - k
w - v
"""
d = {}
for l in m.split('\n'):
    l = l.strip()
    if l:
        print(l)
        f, t = l.split('-')
        d[ord(f.strip())] = ord(t.strip())
        d[ord(f.strip().upper())] = ord(t.strip().upper())

print(txt.translate(d))