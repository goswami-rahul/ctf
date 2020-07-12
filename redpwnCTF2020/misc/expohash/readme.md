# expohash

<https://ctftime.org/writeup/21811>

Let's assume aur keys are in array A[1..N], where N = 10^5.  
For simplicity, A[0] = 0  

Now assume a prefix-xor array of A, P[0..N], such that P[i] = XOR(A[0..i])  

Now, the given tests (L, R, V) imply only one condition, P[R] xor P[L-1] == V  
Note that XOR(A[L..R]) = P[R] xor P[L-1]  

Now, build a graph with N+1 vertices (from 0 to N), and for each test, add edge from (L-1 <-> R) with value V  .

Now for each "connected component" in this graph, set P[node] = 0 (or number) for any one node, and run a dfs from that node setting the neighbor node as its value xor weight of edge.  

Finally you have array P[0..N], now reduce it A[1..N] by A[i] = P[i] xor P[i-1]  
