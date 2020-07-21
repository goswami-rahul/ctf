#!/usr/bin/env python

n = 523693181734689806809285195318

def calc(n):
    count = 0
    while n:
        count += n
        n //= 3
    return count

print(f"csictf{{{calc(n)}}}")