# Picking Up The Pieces

Construct a graph with intersections as vertices, and road as edges with weights.  
Run Dijkstra'a Shortest Path Algorithm on it, atoring the links and trace back to get the actual path.  
Complexity $\mathcal{O}(n \log n)$  

My C++ script

```cpp
#include<bits/stdc++.h>
using namespace std;

const int N = 200000;
vector<pair<int,int>> g[N];
string s[N];
int w[N];
int path[N];
int from[N];

int main() {
    for (int i = 0; i < N; ++i) {
        int u, v;
        cin >> u >> v >> w[i] >> s[i];
        --u, --v;
        g[u].emplace_back(v, i);
        g[v].emplace_back(u, i);
    }
    vector<long long> dis(N, (long long) 1e18);
    dis[0] = 0;
    set<pair<long long, int>> dij;
    dij.emplace(0LL, 0);
    while (!dij.empty()) {
        auto [d, u] = *dij.begin();
        dij.erase(dij.begin());
        for (auto [v, i] : g[u]) {
            long long nd = d + w[i];
            if (nd < dis[v]) {
                dij.erase({dis[v], v});
                dis[v] = nd;
                from[v] = u;
                path[v] = i;
                dij.insert({dis[v], v});
            }
        }
    }
    int u = N - 1;
    vector<int> ord;
    while (u != 0) {
        ord.push_back(path[u]);
        u = from[u];
    }
    reverse(ord.begin(), ord.end());
    for (int i : ord) {
        cout << s[i];
    }
    cout << endl;
}
```

You can see the flag, among other strings in the output

```txt
rgbCTF{1m_b4d_4t_sh0pp1ng}
```
