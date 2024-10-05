# SPDX-License-Identifier: GPL-3.0
# Scraps
#
# Main Makefile
#
# This is really for bulk compiling and testing of each scrap.
#
# COPYRIGHT NOTICE
# Copyright (C) 2024 0x4248 and contributors
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the license is not changed.
# 
# This software is free and open source. Licensed under the GNU general
# public license version 3.0 as published by the Free Software Foundation.
include scraps.mk

# Commands
PYTHON = python3

# Folders
TOOLS = tools

all: 
	@$(PYTHON) $(TOOLS)/scrapbuild.py all $(MK-S)

clean:
	@$(PYTHON) $(TOOLS)/scrapbuild.py clean $(MK-S)

git-ref:
	@git rev-parse HEAD

git-last:
	@git log -1 --pretty=%B%N%an%N%ae%N%at

help:
	@echo "Scrapbuild usage:"
	@echo "make all - Compile all scraps"
	@echo "make clean - Clean all scraps"
	@echo "make help - Show this help message"
	@echo "--GIT--"
	@echo "make git-ref - Get the git reference"
	@echo "make git-last - Get the last commit message"
	@echo "make git-ref git-last - Get both the git reference and last commit message"