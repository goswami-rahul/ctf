filenames = open("filenames.txt").read()
import string
d={}
for name in filenames.splitlines():
    masked_file_name=name.split('_')[1][:-4]
    idx=int(name.split('_')[0])
    password = "".join(
                    [chr((((c - ord("0") - i) % 10) + ord("0")) * int(chr(c) not in string.ascii_lowercase) + (((c - ord("a") - i) % 26) + ord("a")) * int(chr(c) in string.ascii_lowercase))
                    for c, i in zip([ord(a) for a in masked_file_name], range(0xffff))])

    with open("passwords/" + name, "rb") as f:
        d[password]=f.read()
    assert(len(password)==len(d[password]))

# aa=[True]*256
# with open("text_and_cipher1.txt",'wb') as f:
#     for x,v in d.items():
#         s=x.encode()+v
#         f.write(s)
#         for x in s:
#             aa[x]=False
# print(aa)
# for i in range(256):
#     if aa[i]:
#         print(i)