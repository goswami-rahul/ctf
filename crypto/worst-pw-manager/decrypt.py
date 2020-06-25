
def rc4(text, key):  # definitely not stolen from stackoverflow
    S = [i for i in range(256)]
    j = 0
    out = bytearray()

    #KSA Phase
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    #PRGA Phase
    i = j = 0
    for char in text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(char ^ S[(S[i] + S[j]) % 256])

    return bytes(out)

import itertools
import string

pwd = []
enc = []
lns: list = []

def calc(key):
    res = 0
    st = 0
    cyc = itertools.cycle(bytearray(key, 'utf-8'))
    for (e, p) in zip(enc, pwd):
        res += sum(u == v for (u, v) in 
            zip(e, rc4(p, [next(cyc) for _ in range(8)])))
    return res

best = -1
good = []
cands = string.ascii_lowercase + string.digits + '_}'

def brute(key):
    global best, good
    cur = calc(key)
    if cur > best:
        good = [key]
        best = cur
        print(best, key)
    elif cur == best:
        good.append(key)
    if len(key) == 8 or key[-1] == '}':
        return
    if len(key) == 7:
        brute(key + 'g')
        return
    for c in cands:
        brute(key + c)

def read():
    global pwd, enc, lns
    lns = []
    enc = []
    pwd = []
    with open('len.in', 'r') as fp:
        for line in fp:
            lns.append(int(line.strip()))
    with open('enc.in', 'rb') as fp:
        f = fp.read().strip()
        st = 0
        for ln in lns:
            en = st + ln
            enc.append(f[st:en])
            st = en
        assert st == len(f)
    with open('pswd.in', 'rb') as fp:
        f = fp.read().strip()
        st = 0
        for ln in lns:
            en = st + ln
            pwd.append(f[st:en])
            st = en
        assert st == len(f)
    assert len(pwd) == len(enc) == len(lns)

from rich import print
def main():
    global pwd, enc, lns
    read()
    tot = len(lns)
    print(cands, pwd[0], enc[0], len(pwd[0]), len(enc[0]))
    for c in range(256):
        for c2 in range(256):
            for c3 in range(256):
                key = bytearray('flag{', 'utf-8')
                key.extend([c, c2, c3])
                # print(key)
                if enc[0] == rc4(pwd[0], key):
                    print(key)
                # print(enc[0], rc4(pwd[0], bytearray(key, 'utf-8')))
                # exit(0)


    # whr = {}
    # for i, (p, e) in enumerate(zip(pwd, enc)):
    #     x = (p[0] ^ e[0], p[1] ^ e[1], p[2] ^ e[2], p[3] ^ e[3])
    #     if x not in whr:
    #         whr[x] = [i]
    #     else:
    #         whr[x].append(i)
    # print(whr)
    # print(len(whr))

if __name__ == '__main__':
    main()