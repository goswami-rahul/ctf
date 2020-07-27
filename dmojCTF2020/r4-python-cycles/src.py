# uncompyle6 version 3.7.2
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.7.6 | packaged by conda-forge | (default, Jun  1 2020, 18:57:50) 
# [GCC 7.5.0]
# Embedded file name: main.py
# Compiled at: 2020-07-17 21:29:49
# Size of source mod 2**32: 5102 bytes

# int = int
# bytes = bytes
# len = len
# range = range
# pow = pow
# zip = zip
# chr = chr
# 0 = 0
# 1 = 1
# 16 = 16
# 'little' = 'little
# 'big' = 'big
a = b'P\x1e\x05\xa3lQ)\x16B\x84\xe2\xc5\x13\xfbH\x9d\xd43(^\xed\x83\xff\x15\xc6\xbb\x06-k4UJ\xa8t\xb7\xa6\xb570%\x03\xe72\xe0\xe8\xef\xb3M@\xdc\x1fT=h$\x93K\x0e\x86\xa9\\\xb8\xe3\x89\x8f\xf4\xa5+\xf7\xcd\x9aC8Iqf\xfdED#\x0bj\x17\xe1z|:\x80S\xfe\xa1\xd8&\xf3\xd6\xec\xb2\xd3w\x04\xee\xa2\x9f,\x85\x02m\xba\x0c\x1a{9\xdd\xcen\xf8\xb1\x92\x8a\xcb\x8c\x12c\xda\xc7oAg\xd1\xe4\rL\x99\xf1\xfa<\xb6\xca\xcc\xde\xd5 \xa0\xae\x82\xa7\xf5\x9b?\xac\xc3\xbc\xc2\xeb\xf6>\xd0!\x1cb;]\xc0\xb4\x10d\x1daxr\x87\x8e\xeae\xab\x18\xe6O\xbdu\n6\t\x88~\x96\xb0\x07\x00\xd91"\x98\xe5\x94\xfcWy\'\xe9\x19\xaf\xc8\x8d/\xbev\xd7\xcf\x95iX[\x97\x7fZ_\xdf\xc9`\xf9\xadY\xf2VF\xa4\xaa\x81\xc4\x90p\x14*s\x08\x8bN\xbf\x9e\x91}\x11G\xdb.\x9c\xc1\x0f\x01\xb9\x1b\xf0\xd25R'
b = b'\x1e\x13\x04\x03\x14)\t\x17\x12\x07\x0f\x08\x1a"-\x1d\'\x06\x01\r\x16\x10\x02*(\x00!\x11 .\x1b\x05\x18$/\x0b\x19\x1f\x1c+\x0c&#,\x15%\x0e\n'
# print(len(a))  # 256
# print(len(b))  # 48

def rev(arg):
    return int.to_bytes(int.from_bytes(arg, 'little'), len(arg), 'big')


def one(arg):
    return bytes((a[x] for x in arg))


def two(arg):
    # arg = rev(arg)
    # arg = rev(arg)
    return bytes((arg[x] for x in b))


def pad(arg):
    return arg + bytes([16 - len(arg) % 16] * (16 - len(arg) % 16))


def slow(arg):
    arg = pad(arg)
    orig = arg
    i = 0
    while True:
        s = b''
        for j in range(0, len(arg), 16):
            x = arg[j:j + 16]
            x = one(x)
            s += x

        arg = two(s)
        i += 1
        if arg == orig:
            break

    return i


arg = b'\xa0},\x0c@\x0fn5\xfd\xe4\x9a\xc5X\xb9s|\x14E\xe2Z\x92\x9a\x89>\x9e\xaa\xf1\xad\x7f2_|\x97\xaf\xd2p\x99'
# print(len(arg))  # 37


X = b'\xbe\xf5@\xddk"\x80cTH\x87iT\x0b\xa4\x15\x8fp\x8f\x14\x9b\xd1$d\x98\xac\x92\'\x13\x80\xdf[}SH\x9f\xac'
Y = int.to_bytes(pow(slow(arg), 65537, 127314748520905380391777855525586135065716774604121015664758778084648831235208544136462397), len(X), 'big')
print(''.join((chr(x ^ y) for x, y in zip(X, Y))))
# okay decompiling main.cpython-38.pyc
