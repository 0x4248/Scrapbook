# SPDX-License-Identifier: GPL-3.0
# x86bootdisk
#
# Makefile
#
# COPYRIGHT NOTICE
# Copyright (C) 2024 0x4248 and contributors
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the license is not changed.
# 
# This software is free and open source. Licensed under the GNU general
# public license version 3.0 as published by the Free Software Foundation.

NASM = nasm
BOOTDISK = src/boot.asm
OUT = build
BIN = boot.bin

all: init boot

init:
	mkdir -p $(OUT)

boot:
	$(NASM) -f bin $(BOOTDISK) -o $(OUT)/$(BIN) 

clean:
	rm -f $(OUT)/$(BIN)


test: all
	qemu-system-i386 -fda $(OUT)/$(BIN) --bios /Users/lewis/Documents/Code/seabios/out/bios.bin

.PHONY: all clean
