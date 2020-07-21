#!/usr/bin/env python

import requests
from hashlib import sha1
from pwn import *
import string

url = 'http://chall.csivit.com:30272/'

s = "&O&GKtn&54xQ"
res = requests.get(url, params=[('hash', s)])
print(res.text)
