/* SPDX-License-Identifier: GPL-3.0
 * Virtual hardware
 *
 * libbus.h
 * 
 * COPYRIGHT NOTICE
 * Copyright (C) 2024-2025 0x4248 and contributors
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the license is not changed.
 * 
 * This software is free and open source. Licensed under the GNU general
 * public license version 3.0 as published by the Free Software Foundation.
*/


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