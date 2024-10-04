# SPDX-License-Identifier: GPL-3.0
# Fortran file test
#
# Makefile
#
# COPYRIGHT NOTICE
# Copyright (C) 2024 0x4248 and contributors
# This file and software is licenced under the GNU General Public License v3.0. 
# Redistribution of this file and software is permitted under the terms of the 
# GNU General Public License v3.0. 
#
# NO WARRANTY IS PROVIDED WITH THIS SOFTWARE. I AM NOT RELIABLE FOR ANY DAMAGES.
# THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY AND LIABILITY OF ANY KIND.
#
# You should have received a copy of the GNU General Public License v3.0
# along with this program. If you have not please see the following link:
# https://www.gnu.org/licenses/gpl-3.0.html

GFORT = gfortran
OUT = build
BIN = filetest

all: init compile

init:
	mkdir -p $(OUT)

compile:
	$(GFORT) -o $(OUT)/$(BIN) file.f90

clean:
	rm -rf $(OUT)
	rm -rf $(OUT)/$(BIN)

test: all
	$(OUT)/$(BIN)

.PHONY: all clean
