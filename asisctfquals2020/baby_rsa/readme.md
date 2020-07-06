# Baby RSA

We notice that $t_p \equiv 1 \pmod{p}$, so `p` divides both `t_p - 1` and `n`.  
We can calculate `p` as `gcd(n, t_p - 1)`, then `q = n / p` and recover the flag.  

`ASIS{baby___RSA___f0r_W4rM_uP}`
