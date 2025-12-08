# SPDX-License-Identifier: GPL-3.0
# Scrapbook Makefile System
#
# Makefile
# This file seems pretty empty, well thats because it is by design. Check the
# includes in tools/build/make/includes.mk
#
# COPYRIGHT NOTICE
# Copyright (C) 2025 0x4248 and contributors
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the license is not changed.
#
# This software is free and open source. Licensed under the GNU general
# public license version 3.0 as published by the Free Software Foundation.

all: precheck help

NOCONFIG_TARGETS := menuconfig defconfig

precheck:
	$(T)$(LOG) -e "PRECHECK\tGLOBPATH"
	$(T)pwd > .scrappath
	$(T)$(LOG) -e "PRECHECK\tCONFIG"
	@if [ -z "$(filter $(MAKECMDGOALS),$(NOCONFIG_TARGETS))" ]; then \
		if [ ! -f .config ]; then \
			cat doc/make/errors/confmissing.msg | less; \
			exit 1; \
		fi; \
	fi


-include tools/build/make/includes.mk

.PHONY: precheck $(TARGETS)

ifneq ($(filter $(MAKECMDGOALS),$(NOCONFIG_TARGETS)),)
  # This is only ran if they wanted to make the config without any config
else
  $(MAKECMDGOALS): precheck
endif
