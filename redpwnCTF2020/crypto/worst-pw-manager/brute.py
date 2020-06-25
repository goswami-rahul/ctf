def check():
    for length in range(7, 40):
        s = set()
        x = 0
        for i in range(10000):
            s.add(x)
            x = (x + 8) % length
        print(f"len={length}, s={len(s)}")

def get_files():
    import os
    import string
    data = []
    for fn in os.listdir('passwords'):
        idx = int(fn[:fn.find('_')])
        name = ""
        enc = b""
        for i, c in enumerate(fn[fn.find('_') + 1:-4]):
            c = ord(c)
            name += chr((((c - ord("0") - i) % 10) + ord("0")) * int(chr(c) not in string.ascii_lowercase) + 
                (((c - ord("a") - i) % 26) + ord("a")) * int(chr(c) in string.ascii_lowercase))
        with open(f'passwords/{fn}', 'rb') as f:
            enc = f.read()
        name = bytes(name, 'utf-8')
        assert len(name) == len(enc), f"{name}, {enc}"
        data.append((idx, name, enc))
    return sorted(data)

def main():
    files = get_files()
    with open('pswd.in', 'wb') as fp:
        with open('enc.in', 'wb') as fe:
            with open('len.in', 'w') as fl:
                for _, name, enc in files:
                    fp.write(name)
                    fe.write(enc)
                    print(len(enc), file=fl)

if __name__ == '__main__':
    main()