#include<bits/stdc++.h>

ulong f(int x)

{
  uint res;
  int iVar2;
  int iVar3;
  int iVar4;
  int iVar5;
  long lVar6;
  double sqx;
  
  if (x < 4) {
    res = x + 5;
  }
  else {
    sqx = sqrt((double)x);
    iVar5 = f((ulong)(uint)(int)sqx);

    iVar2 = f((ulong)(x - 1));
    iVar3 = f((ulong)(x - 5));
    // lVar6 = x / 3;
    iVar4 = f((ulong)(x / 3);
    res = (iVar5 * 3 + iVar2 + iVar3 + iVar4 * 2) / 3;
  }
  return (ulong)res;
}

int8_t main(void)

{
  int iVar1;
  int32_t uVar2;
  uint uVar3;
  int ctr;
  
  s._0_4_ = f(0xb21f);
  s._4_4_ = f(0xbb2e);
  s._8_4_ = f(0xc41a);
  s._12_4_ = f(0xa64b);
  s._16_4_ = f(0xc0b2);
  iVar1 = f(0);
  uVar2 = f(0xe6ab);
  *(int32_t *)(s + (long)iVar1 * 4) = uVar2;
  iVar1 = f(1);
  uVar2 = f(0xb5c1);
  *(int32_t *)(s + (long)iVar1 * 4) = uVar2;
  iVar1 = f(2);
  uVar2 = f(0xa629);
  *(int32_t *)(s + (long)iVar1 * 4) = uVar2;
  iVar1 = f(3);
  uVar2 = f(0xd5d5);
  *(int32_t *)(s + (long)iVar1 * 4) = uVar2;
  s._36_4_ = f(0xab6e);
  s._40_4_ = f(0xb21f);
  s._44_4_ = f(0xbae9);
  s._48_4_ = f(0xb181);
  s._52_4_ = f(0x5c82);
  s._56_4_ = f(0x6d02);
  iVar1 = f(5);
  uVar2 = f(0xb4aa);
  *(int32_t *)(s + (long)iVar1 * 4) = uVar2;
  s._64_4_ = f(0x4753);
  s._68_4_ = f(0xadc7);
  s._72_4_ = f();

  ctr = 0;
  while (ctr < 0x13) {
    iVar1 = *(int *)(s + (long)ctr * 4);
    if (iVar1 < 0) {
      iVar1 = iVar1 + 0xff;
    }
    putchar(iVar1 >> 8);
    if ((*(uint *)(s + (long)ctr * 4) & 0xff) != 0) {
      uVar3 = (uint)(*(int *)(s + (long)ctr * 4) >> 0x1f) >> 0x18;
      putchar((*(int *)(s + (long)ctr * 4) + uVar3 & 0xff) - uVar3);
    }
    ctr = ctr + 1;
  }
  return 0;
}