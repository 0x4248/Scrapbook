# SPDX-License-Identifier: GPL-3.0
# Scraps
#
# scraps.mk
#
# Each scrap has its own Makefile. This file is used to include all the scraps
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

MK-S += x86bootdisk/Makefile
MK-S += fortran/filetest/Makefile