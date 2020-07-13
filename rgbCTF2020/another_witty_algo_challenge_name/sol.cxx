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