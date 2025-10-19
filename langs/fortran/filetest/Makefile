# SPDX-License-Identifier: GPL-3.0
# Fortran file test
#
# Makefile
#
# COPYRIGHT NOTICE
# Copyright (C) 2024-2025 0x4248 and contributors
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the license is not changed.
#
# This software is free and open source. Licensed under the GNU general
# public license version 3.0 as published by the Free Software Foundation.
include ../../globals.mk

BIN = filetest

all: init compile

init:
	$(S)mkdir -p $(BUILD)

compile:
	$(S)$(GFORT) -o $(BUILD)/$(BIN) file.f90

clean:
	$(S)rm -rf $(BUILD)
	$(S)rm -rf $(BUILD)/$(BIN)

test: all
	$(BUILD)/$(BIN)

.PHONY: all clean
