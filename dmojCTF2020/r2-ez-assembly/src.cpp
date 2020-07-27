#include<bits/stdc++.h>

int main(int param_1,long param_2)

{
  char chr_at_tmpf;
  byte lc;
  char *flag;
  byte rc;
  int len;
  size_t len1;
  char *tmpf;
  byte *j;
  long i;
  int i;
  
  flag = *(char **)(param_2 + 8);
  len1 = strlen(flag);
  len = (int)len1;
  i = 0;
  tmpf = flag;
LAB_00101093:
  do {
    chr_at_tmpf = *tmpf;
    if ((byte)(chr_at_tmpf - '0') < 10) {
      *tmpf = 'i' - chr_at_tmpf;
    }
    else {
      if ((byte)(chr_at_tmpf - 'a') < 26) {
        i = i + 1;
        *tmpf = chr_at_tmpf + -0x24;
        tmpf = tmpf + 1;
        if (len == i) break;
        goto LAB_00101093;
      }
      if ((byte)(chr_at_tmpf - 'A') < 26) {
        *tmpf = chr_at_tmpf + 29;
      }
      else {
        if (chr_at_tmpf == '{') {
          *tmpf = '~';
        }
        else {
          if (chr_at_tmpf == '}') {
            *tmpf = '|';
          }
          else {
            if (chr_at_tmpf == '_') {
              *tmpf = (char)(i % 10) + '!';
            }
          }
        }
      }
    }
    i = i + 1;
    tmpf = tmpf + 1;
  } while (len != i);

  // Reverse
  i = 0;
  j = (byte *)(flag + (long)len + -1);
  do {
    swap(flag[i], flag[j]);
    i = i + 1;
    j = j + -1;
  } while ((int)i < len / 2);

  puts(flag);
  return 0;
}