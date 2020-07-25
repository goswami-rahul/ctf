# pyzzle

We are given a python Concrete Syntax Tree (CST). We can decrypt it using `libcst` library to get source.

```py
from libcst import *

def reverse():
    with open('pyzzle') as f:
        tree = f.read()
    cst = eval(tree)
    with open('src.py', 'w') as f:
        f.write(cst.code)
```

The plaintext is decrypted using a couple XORs on some numbers, we can easily decrypt them to get the plaintext.

The plaintext has our first flag.

```txt
3k{almost_done_shizzle_up_my_nizzle}
```

The text describes a graph, with 2d coordinates as vertices, and some edges between them.  
Format the vertices and edges in good format, on some editor.  
There is an awesome geometry visualization library in C++ [`geodeb`](https://github.com/lukakalinovcic/geodeb) we can use.

```cpp
#include<bits/stdc++.h>
#include "geodeb.h"

using namespace std;

vector<array<int, 2>> edges = {{1, 2}, {2, 3}, /* ... */ {141, 143}, {143, 144}};
vector<array<int, 2>> coord = {{5,5}, {55,5}, /* ... */ {1845,105}};
int main() {
    GD_INIT("points.html");
    // flipped y axis
    for (auto &x : coord) {
        x[1] = 150 - x[1];
    }
    for (auto &e : edges) {
        e[0]--, e[1]--;
    }
    for (auto [u, v] : edges) {
        GD_SEGMENT(coord[u][0], coord[u][1], coord[v][0], coord[v][1]);
    }
}
```

Open the [`points.html`](https://github.com/goswami-rahul/ctf/blob/master/3kCTF2020/pyzzle/points.html) in browser to see the second flag.  

```txt
3k{PYZZLE_FO_SHIZZLE_MY_NIZZLE}
```