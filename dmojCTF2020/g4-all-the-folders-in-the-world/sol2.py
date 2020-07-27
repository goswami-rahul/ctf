#!/usr/bin/env python

from pathlib import Path
from base64 import b64decode
import shutil
from pyunpack import Archive, PatoolError
import logging
import sys

def extract(f: Path):

    pass

dump = []
def walk(p: Path):
    for f in p.iterdir():
        f: Path
        if f.is_file():
            if '.py' in f.name or '.out' in f.name:
                continue
            if f.name.lower().endswith('.iso'):
                continue
            try:
                Archive(f.as_posix()).extractall(p.as_posix())
            except PatoolError as e:
                if '.' in f.name:
                    logging.warning(f"Can't unpack {f.name}")
                # shutil.unpack_archive(f.as_posix(), p.as_posix())
                # extract(f)
            if '.' not in f.name:
                data = f.read_bytes()
                if len(data) == 33:
                    data = b64decode(data)
                    logging.info(f"{f.as_posix().count('/'):0>2}", data)
                    try:
                        print(f"FOUND {data.decode()}")
                    except UnicodeDecodeError:
                        pass
                    if b'ctf' in data:
                        print(f"FOUND {data}")
                    dump.append(data)
    for f in p.iterdir():
        if f.is_dir():
            if 'iso' in f.name.lower():
                logging.warning(f"Skipping {f.name}")
            walk(f)

folder = '.'
if len(sys.argv) > 1:
    folder = sys.argv[1]

walk(Path(folder))

if folder == '.':
    folder = 'main'
with open(f'{folder}.out', 'wb') as f:
    f.write(b'\n'.join(dump))