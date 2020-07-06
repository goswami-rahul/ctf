#!/usr/bin/env python
from Crypto.Util.number import *

enc = 5548605244436176056181226780712792626658031554693210613227037883659685322461405771085980865371756818537836556724405699867834352918413810459894692455739712787293493925926704951363016528075548052788176859617001319579989667391737106534619373230550539705242471496840327096240228287029720859133747702679648464160040864448646353875953946451194177148020357408296263967558099653116183721335233575474288724063742809047676165474538954797346185329962114447585306058828989433687341976816521575673147671067412234404782485540629504019524293885245673723057009189296634321892220944915880530683285446919795527111871615036653620565630
n = 10594734342063566757448883321293669290587889620265586736339477212834603215495912433611144868846006156969270740855007264519632640641698642134252272607634933572167074297087706060885814882562940246513589425206930711731882822983635474686630558630207534121750609979878270286275038737837128131581881266426871686835017263726047271960106044197708707310947840827099436585066447299264829120559315794262731576114771746189786467883424574016648249716997628251427198814515283524719060137118861718653529700994985114658591731819116128152893001811343820147174516271545881541496467750752863683867477159692651266291345654483269128390649
t_p = 4519048305944870673996667250268978888991017018344606790335970757895844518537213438462551754870798014432500599516098452334333141083371363892434537397146761661356351987492551545141544282333284496356154689853566589087098714992334239545021777497521910627396112225599188792518283722610007089616240235553136331948312118820778466109157166814076918897321333302212037091468294236737664634236652872694643742513694231865411343972158511561161110552791654692064067926570244885476257516034078495033460959374008589773105321047878659565315394819180209475120634087455397672140885519817817257776910144945634993354823069305663576529148
e = 65537

p = GCD(n, t_p - 1)
q = n // p
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
flag: int = pow(enc, d, n)
print(long_to_bytes(flag).decode())