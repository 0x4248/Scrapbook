# SPDX-License-Identifier: GPL-3.0
# Scrapbook
#
# Scrapbook.mk
#
# Each scrap has its own Makefile. This file is used to include all the Scrapbook
# so the main Makefile can compile and test each scrap. (If you want to really
# test them all)
# 
# HOW TO ADD A NEW SCRAP:
# 1. Create the makefile
# 2. Add all and clean targets
# 3. Add the makefile to the MK-S variable
#
# This will now allow scrapbuild to see the makefile and compile it.
# 
# COPYRIGHT NOTICE
# Copyright (C) 2024-2025 0x4248 and contributors
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the license is not changed.
#
# This software is free and open source. Licensed under the GNU general
# public license version 3.0 as published by the Free Software Foundation.

MK-S += asm/x86bootdisk/Makefile
MK-S += fortran/filetest/Makefile
MK-S += fortran/matrix/Makefile
MK-S += !c/writing_raw
MK-S += !c/http_server
MK-S += @c/tiny/build.sh
MK-S += !c/factorial
MK-S += !c/XORenc
MK-S += !c/weird_loops