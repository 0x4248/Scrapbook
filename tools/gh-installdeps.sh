# SPDX-License-Identifier: GPL-3.0
# Scraps
#
# Github install dependencies script
#
# Since github actions doesn't always have the required dependencies installed
# we need to install them manually. This script will install the required
# dependencies for the CI to work.
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

sudo apt install -y \
    build-essential \
    cmake \
    gfortran \
    nasm