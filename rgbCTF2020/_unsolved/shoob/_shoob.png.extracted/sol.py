import gzip
with gzip.open('3B.zlib', 'rb') as f:
    s = f.read()
print(s)