#ifdef Rahul
# include "RAHUL.h"
#else
# include <bits/stdc++.h>
  using namespace std;
# define error(...) 42;
#endif
#define SZ(v) int((v).size())
#define ALL(vec) begin(vec), end(vec)
typedef long long i64;
template<typename T> inline bool uax(T &x, T y) {return (y > x) ? x = y, true : false;}
template<typename T> inline bool uin(T &x, T y) {return (y < x) ? x = y, true : false;}
template<typename T> void kek(T ans) {cout << ans << endl; exit(0);}
#define Lu(...) [&] (auto &&u) { return __VA_ARGS__; }
#define Luv(...) [&] (auto &&u, auto &&v) { return __VA_ARGS__; }
const int MOD = (int) 1e9 + 7;
const i64 INF = (i64) 1e18 + 42;

int main() {
  cin.tie(nullptr) -> sync_with_stdio(false);
  
  const int n = (int) 1e5;
  vector<int> l(n), r(n), v(n);
  vector<vector<pair<int, int>>> g(n + 1);
  for (int i = 0; i < n; ++i) {
    cin >> l[i] >> r[i] >> v[i];
    g[l[i] - 1].push_back({r[i], v[i]});
    g[r[i]].push_back({l[i] - 1, v[i]});
  }
  error("donereading");
  vector<int> ans(n + 1, -1);
  for (int s = 0; s <= n; ++s) if (ans[s] == -1) {
    ans[s] = 0;
    vector<int> bfs = {s};
    for (int i = 0; i < SZ(bfs); ++i) {
      int u = bfs[i];
      for (auto [w, x] : g[u]) {
        if (~ans[w]) assert (ans[w] == (x ^ ans[u]));
        else ans[w] = x ^ ans[u], bfs.push_back(w);
      }
    }
  }
  for (int i = n; i > 0; --i) {
    ans[i] ^= ans[i - 1];
  }
  error("doneprocessing");
  for (int i = 1; i <= n; ++i) {
    cout << ans[i] << endl;
  }
  error("donewriting");
  string flag;
  cin >> flag;
  error(flag);
}
