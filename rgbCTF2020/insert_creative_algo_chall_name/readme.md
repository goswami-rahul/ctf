# [insert creative algo chall name]

First, let's say we want to count the ways as $f(x, n)$ with $x$ and $n$ as mentioned in the statement.  
If we fix the largest number in our partition, we see that it always uses the most significant bit in it ($2^{n-1}$). So, we use it and we can choose any bits from the remaining $n-1$ bits.  
Say we choose 2 other bits, now we have $n-3$ bits remaining, and $x-1$ parts to partition. So we can solve it recursively (with memoization ofcourse).  

The recurrance is

$$f(x, n) = \sum\limits_{i=0}^{n-1}{{n-1}\choose{i}}\cdot f(x-1, n-1-i)$$  

My C++ script

```cpp
#include<bits/stdc++.h>

int ncr[13][13];
int dp[5][13];

int calc(int x, int n) {
    if (n == 0) return 0;
    if (x == 1) return 1;
    int &res = dp[x][n];
    if (~res) return res;
    res = 0;
    for (int t = 0; t < n; ++t) {
        res += ncr[n - 1][t] * calc(x - 1, n - 1 - t);
    }
    return res;
}

int main() {
    const int X = 4, N = 12;
    memset(dp, -1, sizeof dp);
    for (int i = 0; i <= N; ++i) {
        ncr[i][0] = 1;
        for (int j = 1; j <= i; ++j) {
            ncr[i][j] = ncr[i - 1][j] + ncr[i - 1][j - 1];
        }
    }
    std::cout << "rgbCTF{" << calc(X, N) << "}" << std::endl;
}
```

Flag

```txt
rgbCTF{611501}
```
