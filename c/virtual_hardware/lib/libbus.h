#include<stdbool.h>
#include "lib/libbit.h"

typedef bit bus_4[4];

typedef bus_4 nibble;

typedef struct {
    bit bus[8];
} bus_8;

typedef bus_8 byte;

typedef struct {
    bit bus[16];
} bus_16;

typedef struct {
    bit bus[32];
} bus_32;

typedef struct {
    bit bus[64];
} bus_64;