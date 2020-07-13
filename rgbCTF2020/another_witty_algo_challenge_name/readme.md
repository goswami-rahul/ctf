# [another witty algo challenge name]

## Statement

This is pretty simple. You get a list of 5000 by 5000 grid of ones and zeros, and you have to print the number of islands in the grid.

An island is a collections of ones where each one is adjacent to another one in the island. For a cell to be adjacent to another cell, they must share an edge.

Submit the number wrapped in the flag format, like rgbCTF{123}

---

Initially mark all the cells with `0` as visited.
Loop through all the cells of the grid, when find an unmarked cell, increment the islands count, and find its island and mark all its cells as visited using dfs from the cell. Complexity $\mathcal{O}(n^2)$.  

My C++ script

```cpp
#include <bits/stdc++.h>

const int N = 5000;
char grid[N][N];

void dfs(int x, int y) {
    if (x < 0 or y < 0 or x >= N or y >= N or grid[x][y] == '0') {
        return;
    }
    grid[x][y] = '0';
    dfs(x + 1, y);
    dfs(x - 1, y);
    dfs(x, y + 1);
    dfs(x, y - 1);
}
int main() {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            std::cin >> grid[i][j];
        }
    }
    int islands = 0;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (grid[i][j] == '1') {
                ++islands;
                dfs(i, j);
            }
        }
    }
    std::cout << "rgbCTF{" << islands << "}" << std::endl;
}
```

Flag

```txt
rgbCTF{119609}
```
