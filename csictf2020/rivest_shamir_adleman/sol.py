#!/usr/bin/env python
from Crypto.Util.number import *

phi = 408579120322559108971841469124848503258474925184086139548833106688770638488565627633198182607013895445354251771442359038429937414167181589307913754359396477104727102263157011988136721549122783277478724262191709545597184123942240855574393608022907658836225632844247632699974069178210075740249216128470998584630713277740385076547512621785826119966545869523217190040845172547694126237683215971908137183971439798396759609787472175362989759637473718491321532313974929404180248280920189014452204246207232
n = 408579146706567976063586763758203051093687666875502812646277701560732347095463873824829467529879836457478436098685606552992513164224712398195503564207485938278827523972139196070431397049700119503436522251010430918143933255323117421712000644324381094600257291929523792609421325002527067471808992410166917641057703562860663026873111322556414272297111644069436801401012920448661637616392792337964865050210799542881102709109912849797010633838067759525247734892916438373776477679080154595973530904808231
e = 65537
c = 226582271940094442087193050781730854272200420106419489092394544365159707306164351084355362938310978502945875712496307487367548451311593283589317511213656234433015906518135430048027246548193062845961541375898496150123721180020417232872212026782286711541777491477220762823620612241593367070405349675337889270277102235298455763273194540359004938828819546420083966793260159983751717798236019327334525608143172073795095665271013295322241504491351162010517033995871502259721412160906176911277416194406909

d = inverse(e, phi)
f = pow(c, d, n)
print(long_to_bytes(f).decode())