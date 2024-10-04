# SPDX-License-Identifier: GPL-3.0
# Scraps
#
# Main Makefile
#
# This is really for bulk compiling and testing of each scrap.
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

include scraps.mk

all: 
	@python3 tools/scrapbuild.py all $(MK-S)

clean:
	@python3 tools/scrapbuild.py clean $(MK-S)

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