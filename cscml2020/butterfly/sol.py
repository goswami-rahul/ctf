#!/usr/bin/env python

def main():
    for char in utf8_iterator():
        if len(char) == 1 and len(char.upper()) == 2:
            print(char, char.upper())
            break

# from https://github.com/Lucas-C/dotfiles_and_notes/blob/master/languages/python/utf8_iterator.py
import itertools

def byte_iterator(start, end):
    for i in range(start, end):
        yield bytes((i,))

def utf8_bytestring_iterator():
    # Doc: https://en.wikipedia.org/wiki/UTF-8#Description & https://fr.wikipedia.org/wiki/UTF-8#Description
    yield from byte_iterator(0x00, 0x80)  # 2^7 characters
    for i, j in itertools.product(byte_iterator(0xc0, 0xe0),
                                  byte_iterator(0x80, 0xc0)):  # 2^11 characters
        yield b''.join((i, j))  # Some additional restrictions could be applied here (start=0xc2)
    for i, j, k in itertools.product(byte_iterator(0xe0, 0xf0),
                                     byte_iterator(0x80, 0xc0),
                                     byte_iterator(0x80, 0xc0)):  # 2^16 characters
        yield b''.join((i, j, k))  # Some additional restrictions could be applied here
    for i, j, k, l in itertools.product(byte_iterator(0xf0, 0xf8),
                                        byte_iterator(0x80, 0xc0),
                                        byte_iterator(0x80, 0xc0),
                                        byte_iterator(0x80, 0xc0)):  # 2^21 characters
        yield b''.join((i, j, k, l))  # Some additional restrictions could be applied here

def utf8_iterator():
    for bytestring in utf8_bytestring_iterator():
        try:
            yield bytestring.decode('utf8')
        except UnicodeError:
            pass

if __name__ == '__main__':
    main()
