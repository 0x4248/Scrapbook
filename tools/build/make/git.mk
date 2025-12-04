# SPDX-License-Identifier: GPL-3.0
# Scrapbook Makefile System
#
# git.mk
# GIT based targets
#
# COPYRIGHT NOTICE
# Copyright (C) 2025 0x4248 and contributors
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the license is not changed.
#
# This software is free and open source. Licensed under the GNU general
# public license version 3.0 as published by the Free Software Foundation.

g-log:
	$(T)$(LOG) -e "GIT\tLOG"
	$(T)git log

g-acp:
	$(T)$(LOG) -e "GIT\t ADD > COMMIT > PUSH"
	$(T)git add *
	$(T)git commit --signoff
	$(T)git push

g-mod:
	$(T)git submodule update --recursive --remote

TARGETS += g-log g-acp
