//
// This file was generated by the Retargetable Decompiler
// Website: https://retdec.com
// Copyright (c) Retargetable Decompiler <info@retdec.com>
//

#include <math.h>
#include <stdint.h>
#include <stdio.h>

// ---------------- Integer Types Definitions -----------------

typedef int64_t int128_t;

// ----------------- Float Types Definitions ------------------

typedef float float32_t;
typedef double float64_t;

// ------------------- Function Prototypes --------------------

int64_t __do_global_dtors_aux(void);
int64_t __libc_csu_fini(void);
int64_t __libc_csu_init(void);
int64_t _fini(void);
int64_t _init(void);
int64_t _start(void);
int64_t deregister_tm_clones(void);
int64_t f(int64_t a1);
int64_t frame_dummy(void);
int64_t function_1003(void);
int32_t function_1030(int32_t c);
float64_t function_1040(float64_t a1);
int64_t function_10f3(void);
int64_t function_1143(void);
int64_t function_1463(int64_t a1, int64_t a2, int64_t a3);
int64_t function_14d3(void);
int64_t function_14db(void);
int64_t register_tm_clones(void);

// --------------------- Global Variables ---------------------

int64_t g1 = 0x1140; // 0x3dd8
int64_t g2 = 0x10f0; // 0x3de0
int64_t g3 = 0; // 0x3ff8
char g4 = 0; // 0x4040
int64_t g5 = 0; // 0x4060
int64_t g6 = 0; // 0x4064
int64_t g7 = 0; // 0x4068
int64_t g8 = 0; // 0x406c
int64_t g9 = 0; // 0x4070
int64_t g10 = 0; // 0x4084
int64_t g11 = 0; // 0x4088
int64_t g12 = 0; // 0x408c
int64_t g13 = 0; // 0x4090
int64_t g14 = 0; // 0x4094
int64_t g15 = 0; // 0x4098
int64_t g16 = 0; // 0x40a0
int64_t g17 = 0; // 0x40a4
int64_t g18 = 0; // 0x40a8
int32_t g19;

// ------------------------ Functions -------------------------

// Address range: 0x1000 - 0x1001
int64_t _init(void) {
    // 0x1000
    int64_t result; // 0x1000
    return result;
}

// Address range: 0x1003 - 0x101b
int64_t function_1003(void) {
    int64_t result = 0; // 0x1012
    if (*(int64_t *)0x3fe8 != 0) {
        // 0x1014
        __gmon_start__();
        result = &g19;
    }
    // 0x1016
    return result;
}

// Address range: 0x1030 - 0x1036
int32_t function_1030(int32_t c) {
    // 0x1030
    return putchar(c);
}

// Address range: 0x1040 - 0x1046
float64_t function_1040(float64_t a1) {
    // 0x1040
    return sqrt(a1);
}

// Address range: 0x1050 - 0x1051
int64_t _start(void) {
    // 0x1050
    int64_t result; // 0x1050
    return result;
}

// Address range: 0x1080 - 0x10a9
int64_t deregister_tm_clones(void) {
    // 0x1080
    return 0x4038;
}

// Address range: 0x10b0 - 0x10e9
int64_t register_tm_clones(void) {
    // 0x10b0
    return 0;
}

// Address range: 0x10f0 - 0x10f1
int64_t __do_global_dtors_aux(void) {
    // 0x10f0
    int64_t result; // 0x10f0
    return result;
}

// Address range: 0x10f3 - 0x1131
int64_t function_10f3(void) {
    // 0x10f3
    if (g4 != 0) {
        // 0x1130
        int64_t result; // 0x10f3
        return result;
    }
    // 0x10fd
    if (g3 != 0) {
        // 0x110b
        __cxa_finalize((int64_t *)*(int64_t *)0x4030);
    }
    int64_t result2 = deregister_tm_clones(); // 0x1118
    g4 = 1;
    return result2;
}

// Address range: 0x1140 - 0x1141
int64_t frame_dummy(void) {
    // 0x1140
    int64_t result; // 0x1140
    return result;
}

// Address range: 0x1143 - 0x1149
int64_t function_1143(void) {
    // 0x1143
    return register_tm_clones();
}

// Address range: 0x1149 - 0x11f3
// Demangled:     float
int64_t f(int64_t a1) {
    int64_t v1 = 0x100000000 * a1 / 0x100000000; // 0x1152
    int64_t result; // 0x1149
    if ((int32_t)a1 > 3) {
        int64_t v2 = f(v1 + 0xffffffff & 0xffffffff); // 0x116e
        int64_t v3 = f(v1 + 0xfffffffb & 0xffffffff); // 0x117d
        int32_t v4 = v1; // 0x1195
        int64_t v5 = f((int64_t)((int32_t)(0x55555556 * v1 / 0x100000000) - (v4 >> 31))); // 0x11a0
        int128_t v6; // 0x1149
        __asm_pxor(v6, v6);
        int128_t v7 = __asm_movq_1(__asm_movq(__asm_cvtsi2sd(v4))); // 0x11b7
        uint32_t v8 = __asm_cvttsd2si((int128_t)(int32_t)(float32_t)sqrt((float64_t)(int64_t)v7)); // 0x11c1
        int64_t v9 = v3 + v2 + 2 * v5 + 3 * f((int64_t)v8); // 0x11d4
        result = (int32_t)(0x55555556 * 0x100000000 * v9 / 0x100000000 / 0x100000000) - ((int32_t)v9 >> 31);
    } else {
        // 0x115b
        result = v1 + 5 & 0xffffffff;
    }
    // 0x11ed
    return result;
}

// Address range: 0x11f3 - 0x1452
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

// Address range: 0x1460 - 0x1461
int64_t __libc_csu_init(void) {
    // 0x1460
    int64_t result; // 0x1460
    return result;
}

// Address range: 0x1463 - 0x14c5
int64_t function_1463(int64_t a1, int64_t a2, int64_t a3) {
    int64_t result = _init(); // 0x148c
    if ((int64_t)&g2 - (int64_t)&g1 >> 3 == 0) {
        // 0x14b6
        return result;
    }
    int64_t v1 = 0; // 0x1495
    while (v1 + 1 != (int64_t)&g2 - (int64_t)&g1 >> 3) {
        // 0x14a0
        v1++;
    }
    // 0x14b6
    return result;
}

// Address range: 0x14d0 - 0x14d1
int64_t __libc_csu_fini(void) {
    // 0x14d0
    int64_t result; // 0x14d0
    return result;
}

// Address range: 0x14d3 - 0x14d5
int64_t function_14d3(void) {
    // 0x14d3
    int64_t result; // 0x14d3
    return result;
}

// Address range: 0x14d8 - 0x14d9
int64_t _fini(void) {
    // 0x14d8
    int64_t result; // 0x14d8
    return result;
}

// Address range: 0x14db - 0x14e5
int64_t function_14db(void) {
    // 0x14db
    int64_t result; // 0x14db
    return result;
}

// --------------- Dynamically Linked Functions ---------------

// void __cxa_finalize(void * d);
// void __gmon_start__(void);
// int putchar(int c);
// double sqrt(double);

// --------------------- Meta-Information ---------------------

// Detected compiler/packer: gcc (10.1.0)
// Detected functions: 19
