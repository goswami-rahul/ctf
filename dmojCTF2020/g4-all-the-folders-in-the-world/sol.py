#!/usr/bin/env python

from pathlib import Path
from base64 import b64decode
import shutil

def extract(f: Path):
    pass

dump = []
def walk(p: Path):
    for f in p.iterdir():
        f: Path
        if f.is_file():
            print(f.name)
            if '.py' in f.name or '.out' in f.name:
                continue
            if '.' in f.name:
                print(f"[+] Extract {f.name}")
                shutil.unpack_archive(f.as_posix(), p.as_posix())
                # extract(f)
            else:
                data = b64decode(f.read_bytes())
                print(f"{f.as_posix().count('/'):0>2}", data)
                dump.append(data)
    for f in p.iterdir():
        if f.is_dir():
            walk(f)

walk(Path('.'))

with open('flags.out', 'wb') as f:
    f.write(b'\n'.join(dump))