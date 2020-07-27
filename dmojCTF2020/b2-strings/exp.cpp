#include <bits/stdc++.h>
using namespace std;

int main() {
  char flag[64];
  FILE *f = fopen("flag", "r");
  fgets(flag, 64, f);
  printf(flag);
  return 0;
}
