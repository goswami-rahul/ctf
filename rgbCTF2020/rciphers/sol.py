#!/usr/bin/env python
import string
txt = """
Nfwp wp z hkakzudfzoinwj plopnwnlnwka jwdfix, yfwjf jza oi znnzjgit ywnf mxicliajs zazuspwp. 
Zunfklqf nfwp znnzjg jza oi tkai os fzat, wn'p lplzuus hljf izpwix nk lpi z dxkqxzh nk tk wn mkx skl. 
Nyk qkkt yiopwnip nfzn ywuu tijxsdn plopnwnlnwka jwdfixp mkx skl zxi zn qlozuuz.ti/plopnwnlnwka-pkuvix zat clwdcwld.jkh. 
Wm skl fzvia'n nxwit nfih oimkxi, skl pfklut jfijg nfih kln. Fixi'p sklx muzq: xqoJNM{blpn_4pg_nf3_wan3xa3n_n0_t3jxsdn_wn}
Zupk, Zuij oiuwivip wn'p vixs whdkxnzan nfzn skl pii nfwp: fnndp://w.xitt.wn/1d7y8g0272851.bdq
"""

S = "fndpxqojnmzwibaygtusclkh"
T = "htpsrgbctfaiejnwkdlyquom"
print(txt.translate(str.maketrans(S + S.upper(), T + T.upper())))