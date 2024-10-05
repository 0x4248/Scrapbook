/* SPDX-License-Identifier: GPL-3.0
 * writing_raw
 *
 * write.c
 *
 * COPYRIGHT NOTICE
 * Copyright (C) 2024 0x4248 and contributors
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the license is not changed.
 * 
 * This software is free and open source. Licensed under the GNU general
 * public license version 3.0 as published by the Free Software Foundation.
*/

#include <stdio.h>
#include <stdint.h>

#include "write.h"

int write_data(const uint8_t data[], 
				const char *filename, 
				const int buffer_size) {
	FILE *file = fopen(filename, "wb");
	if (file == NULL) {
		perror("fopen");
		return -1;
	}

	size_t written = fwrite(data, sizeof(uint8_t), buffer_size, file);
	if (written != buffer_size) {
		perror("fwrite");
		fclose(file);
		return -1;
	}

	fclose(file);
	return 0;
}