filenames = open("filenames.txt").read()
import string
from collections import defaultdict
NN=500
dc=[0]*NN
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
        dc[idx]=fg

dd=[]
for p in range(NN):
    for i in range(NN-p):
        if dc[i]==0 or dc[i+p]==0:
            continue
        ll=min(len(dc[i]),len(dc[i+p]))
        if dc[i][:ll]!=dc[i+p][:ll]:
            break
    else:
        dd.append(p)
print(dd)
