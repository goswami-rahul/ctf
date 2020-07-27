#!/usr/bin/env python
import re

def main():
    LIM = 100000
    f = [None] * LIM
    for x in range(LIM):
        if x == 4:
            f[x] = 0xf
        elif x < 4:
            f[x] = x + 5
        else:
            f[x] = (f[x - 1] + f[x - 5] + f[x // 3] * 2 + f[int(x ** 0.5)] * 3) // 3

    m = re.findall('\(0x(....)\)', ugly)
    flag = []
    for i, x in enumerate(m):
        if i == 15:  # special
            continue
        x = f[int(x, 16)]
        if i in (13, 14):  # special
            x = f[x]
        flag.extend(divmod(x, 1 << 8))
    flag = bytes(flag).decode()
    print(flag)

# from retdec
ugly = """
int main(int argc, char ** argv) {
    int64_t v1 = f(0xb21f); // 0x1201
    *(int32_t *)&g5 = (int32_t)v1;
    int64_t v2 = f(0xbb2e); // 0x1211
    *(int32_t *)&g6 = (int32_t)v2;
    int64_t v3 = f(0xc41a); // 0x1221
    *(int32_t *)&g7 = (int32_t)v3;
    int64_t v4 = f(0xa64b); // 0x1231
    *(int32_t *)&g8 = (int32_t)v4;
    int64_t v5 = f(0xc0b2); // 0x1241
    *(int32_t *)&g9 = (int32_t)v5;
    int64_t v6 = f(0); // 0x1251
    int64_t v7 = f(0xe6ab); // 0x125d
    *(int32_t *)(0x100000000 * v6 / 0x40000000 + (int64_t)&g5) = (int32_t)v7;
    int64_t v8 = f(1); // 0x127c
    int64_t v9 = f(0xb5c1); // 0x1288
    *(int32_t *)(0x100000000 * v8 / 0x40000000 + (int64_t)&g5) = (int32_t)v9;
    int64_t v10 = f(2); // 0x12a7
    int64_t v11 = f(0xa629); // 0x12b3
    *(int32_t *)(0x100000000 * v10 / 0x40000000 + (int64_t)&g5) = (int32_t)v11;
    int64_t v12 = f(3); // 0x12d2
    int64_t v13 = f(0xd5d5); // 0x12de
    *(int32_t *)(0x100000000 * v12 / 0x40000000 + (int64_t)&g5) = (int32_t)v13;
    int64_t v14 = f(0xab6e); // 0x12fd
    *(int32_t *)&g10 = (int32_t)v14;
    int64_t v15 = f(0xb21f); // 0x130d
    *(int32_t *)&g11 = (int32_t)v15;
    int64_t v16 = f(0xbae9); // 0x131d
    *(int32_t *)&g12 = (int32_t)v16;
    int64_t v17 = f(0xb181); // 0x132d
    *(int32_t *)&g13 = (int32_t)v17;
    int64_t v18 = f(f(0x5c82) & 0xffffffff); // 0x1344
    *(int32_t *)&g14 = (int32_t)v18;
    int64_t v19 = f(f(0x6d02) & 0xffffffff); // 0x135b
    *(int32_t *)&g15 = (int32_t)v19;
    int64_t v20 = f(5); // 0x136b
    int64_t v21 = f(0xb4aa); // 0x1377
    *(int32_t *)(0x100000000 * v20 / 0x40000000 + (int64_t)&g5) = (int32_t)v21;
    int64_t v22 = f(0x4753); // 0x1396
    *(int32_t *)&g16 = (int32_t)v22;
    int64_t v23 = f(0xadc7); // 0x13a6
    *(int32_t *)&g17 = (int32_t)v23;
    int64_t v24 = f(0xf959); // 0x13b6
    *(int32_t *)&g18 = (int32_t)v24;
    for (int64_t i = 0; i < 19; i++) {
        int32_t * v25 = (int32_t *)(4 * i + (int64_t)&g5); // 0x13de
        int32_t v26 = *v25; // 0x13de
        putchar((v26 < 0 ? v26 + 255 : v26) / 256);
        uint32_t v27 = *v25; // 0x140a
        if (v27 % 256 != 0) {
            // 0x1414
            putchar(v27 % 256);
        }
    }
    // 0x1447
    return 0;
}
"""

main()