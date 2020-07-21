#!/usr/bin/env python
import re

def dec2(text, key):
    k = [key[i % len(key)] for i in range(len(text))]
    return ''.join([chr(ord(text[i]) ^ ord(k[i]) + ord('a')) for i in range(len(text))])


def dec3(text):
    mapping = [28, 33, 6, 17, 7, 41, 27, 29, 31, 30, 39, 21, 34, 15, 3, 5, 13, 10, 19, 38, 40, 14, 26, 25, 32, 0, 36, 8, 18, 4, 1, 11, 24, 2, 37, 20, 23, 35, 22, 12, 16, 9]

    temp = [None]*len(text)
    for i in range(len(text)):
        temp[i] = text[mapping[i]]
    
    return ''.join(temp)

def dec4(text):
    mapping = [23, 9, 5, 6, 22, 28, 25, 30, 15, 8, 16, 19, 24, 11, 10, 7, 2, 14, 18, 1, 29, 21, 12, 4, 20, 0, 26, 13, 17, 3, 27]

    temp = [None]*len(text)
    for i in range(len(text)):
        temp[mapping[i]] = text[i]
    
    return ''.join(temp)

key = 'ieluvnvfgvfahuxhvfphbppnbgrfcrn'
enc = '»·­ª»£µ±¬¥¼±ºµ±¿·£¦­´¯ª¨¥«¥¦«´¸¦¡¸¢²§¤¦¦¹¨'

key = dec4(dec4(key))

for i in range(26):
    nkey = ''.join(chr((ord(c) - 97 + i) % 26 + 97) for c in key)
    text = dec2(dec3(dec3(enc)), nkey)
    for j in range(26):
        text = ''.join(chr((ord(c) - 97 + 1) % 26 + 97) for c in text)
        if 'csictf' in text:
            flag = text[:6] + '{' + text[7:-1] + '}'
            print(flag)
