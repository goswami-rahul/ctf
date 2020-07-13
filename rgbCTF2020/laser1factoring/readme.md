# Laser 1 - Factoring

I enjoyed solving this. I wrote a O(n) algorithm to generate the factors.  
It can be tricky because we have to output them in ascending order.
Since the stack is reversed, I had to iterate on numbers n to 1 in decreasing order, inserting the factors in a separate stack.

factors.lsr

```txt
rsrU>⌝rwD%⌝prU>(\
     U    p    
     #    r   
          U
          r    
          s    
          \   /   
    \           /
```

It passes all tests and get the flag

```txt
rgbCTF{l4s3rs_4r3_c00l_r1ght}
```
