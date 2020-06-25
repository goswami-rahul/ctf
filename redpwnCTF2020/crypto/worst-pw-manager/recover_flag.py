filenames = open("filenames.txt").read()
import string
from collections import defaultdict
dc=defaultdict(int)
for name in filenames.splitlines():
    masked_file_name=name.split('_')[1][:-4]
    idx=int(name.split('_')[0])
    password = "".join(
                    [chr((((c - ord("0") - i) % 10) + ord("0")) * int(chr(c) not in string.ascii_lowercase) + (((c - ord("a") - i) % 26) + ord("a")) * int(chr(c) in string.ascii_lowercase))
                    for c, i in zip([ord(a) for a in masked_file_name], range(0xffff))])

    with open("passwords/" + name, "rb") as f:
        cipher=f.read()
        fg=""
        for x,y in zip(password,cipher):
            fg+=chr(ord(x)^ord(y))
        dc[fg]+=1

aaaa=[x for x in dc.items()]
aaaa.sort(key=lambda v:v[1],reverse=True)
print(aaaa)

valid_chars="_"+string.ascii_lowercase
for i in range(10):
    valid_chars+=chr(ord('0')+i)
print(valid_chars)

class KeyByteHolder(): # im paid by LoC, excuse the enterprise level code
    def __init__(self, num):
        assert num >= 0 and num < 256
        self.num = num

    def __repr__(self):
        return hex(self.num)[2:]

def generate_key(flag):
    key = [KeyByteHolder(0)] * 8 # TODO: increase key length for more security?
    for i, c in enumerate(flag): # use top secret master password to encrypt all passwords
        key[i].num = ord(c)
    return key

def rc4(key): # definitely not stolen from stackoverflow
    S = [i for i in range(256)]
    j = 0
    out = ""

    #KSA Phase
    for i in range(256):
        j = (j + S[i] + key[i % len(key)].num) % 256
        S[i] , S[j] = S[j] , S[i]
    N=10
    #PRGA Phase
    i = j = 0
    for _ in range(N):
        i = ( i + 1 ) % 256
        j = ( j + S[i] ) % 256
        S[i] , S[j] = S[j] , S[i]
        out+=chr(S[(S[i] + S[j]) % 256])

    return out

def find_next(flag):
    def count_matches(flag):
        key=generate_key(flag)
        ss=rc4(key)
        cnt=0
        for xr,val in dc.items():
            if xr==ss[:len(xr)]:
                cnt+=val
                # print(xr,val)
        return cnt

    mtd={}
    for x in valid_chars:
        for y in valid_chars:
            cnt=count_matches(flag+x+y)
            if cnt:
                mtd[x+y]=cnt

    if not mtd:
        return ""
    a=[x for x in mtd]
    a.sort(key=lambda v:mtd[v],reverse=True)
    print(len(mtd))
    # print(flag)
    for i in range(len(mtd)):
        if mtd[a[0]]!=mtd[a[i]]:
            print(flag,i,a[:i])
            break
    return a[0]

# del dc['newyork']

flag="flag{"
print(flag)
# while flag[-1]!='}' and len(flag)<80:
for xy in valid_chars:
# while True:
    print("finding next")
    nxt=find_next(flag+xy)
    print(flag+xy,nxt)
    # break