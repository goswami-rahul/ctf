# Slowest Algorithm

<https://ctftime.org/writeup/22208>  

We basically need to optimize the following algorithm

```py
def decrypt(c):
    N = len(c)  # N = 20000
    ret = 0
    for P in product(range(N), repeat = N):
        ret += reduce(gcd, P) * sum(i * c[P[i]] for i in range(N))
    return ret % MOD
```

The runtime of above algorithm is $\mathcal{O}(n^{n+1}\cdot \log{n})$, which too slow for $n = 20000$ to complete.  
We can compute the sum in $\mathcal{O}(n^2 \log n)$.  

If we compute the sum for the terms with fixed gcd $g$. the sum can be rewitten as the following using symmetry  
$$ \sum\limits_{g} {\sum\limits_{P_{0\dots n-1} : gcd(P_{0\dots n-1})=g}{} g \cdot P_0 \cdot \frac{n \cdot (n-1)}{2} } $$  

Let's fix $P_0$ and iterate over its value in $[0, n)$. Now for each $P_0$ we add its contribution  

- Let $cnt_t$ be count number of tuples of $n-1$ length ($P_{1\dots n-1}$), with values in $[0,n)$, such that $gcd(P_{1\dots n-1}) = t$, for each $t$ in $[0, n)$  
- $P_0$ contributes $gcd(t, P_0) \cdot cnt_t$ to the final sum.  

Finally multiply the result with $ \frac{n \cdot (n-1)}{2} $ (sum of first $n$ non negative numbers)

We can calculate $cnt_t$ once, in $\mathcal{O}(n \cdot \log n)$ using the following algorithm  

- $cnt_0 = 1$  
- $cnt_i = u^{n-1} - \sum\limits_{\forall j : i \vert j} cnt_j$, where $u$ is the count of numbers in $[0, n)$ divisible by $i$  

Final script  

```py
#!/usr/bin/env python
from math import gcd
import json
from rich.progress import track
import sys

MOD = 69366296890289401502186466714324091327187023250181223675242511147337714372850256205482719088016822121023725770514726086328879208694006471882354415627744263559950687914692211431491359503896279403796581365981225023065749656346527652480289235008956593933928571457700779656030733229310882472880060831832351425517

def solve(c):
    N = len(c)
    dp = [0] * N
    dp[0] = 1
    for i in range(N - 1, 0, -1):
        u = (N - 1) // i + 1
        dp[i] = pow(u, N - 1, MOD) - dp[0]
        for j in range(i + i, N, i):
            dp[i] -= dp[j]
        dp[i] %= MOD
    res = 0
    for i in track(range(N)):
        s = 0
        for g in range(N):
            s += dp[g] * gcd(g, i) % MOD
            if s >= MOD:
                s -= MOD
        res += c[i] * s % MOD
        if res >= MOD:
            res -= MOD
    return res * (N * (N - 1) // 2) % MOD


with open('encrypted.json') as f:
    encrypted = json.load(f)
flag = solve(encrypted)
print(flag.to_bytes((flag.bit_length() + 7) // 8, byteorder='big').decode())
```

Prints the flag  

```txt
TSGCTF{GRE4T!_y0u_Found_n1c3_decription_Alg0r1thm_or_you_h4ve_aston1shing_Fa5t_c4lcul4t0r}
```
