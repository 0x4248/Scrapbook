# SPDX-License-Identifier: GPL-3.0
# Scraps
#
# Scrapbuild.py
# Makefile runner
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

import sys
import subprocess
import os

RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"
BLUE = "\033[34m"

def main():
	print(f"{BLUE}STARTING SCRAPBUILD{RESET}")
	TYPE = sys.argv[1]
	MAKEFILES = sys.argv[2:]
	if MAKEFILES == []:
		print("No makefiles specified.")
		sys.exit(1)
	current = 0
	ROOT = os.getcwd()
	if TYPE not in ["clean", "all"]:
		print("Invalid type. Use 'clean' or 'all'.")
		sys.exit(1)
	if TYPE == "clean":
		print(f"{BLUE}Cleaning makefiles.{RESET}")
	elif TYPE == "all":
		print(f"{BLUE}Building makefiles.{RESET}")
	for makefile in MAKEFILES:
		os.chdir(os.path.dirname(makefile))
		print(f"[{GREEN}{current/len(MAKEFILES)*100}%{RESET}] {GREEN}{makefile}{RESET}")
		current += 1
		try:
			if TYPE == "clean":
				subprocess.run(["make", "clean"], check=True)
			elif TYPE == "all":
				subprocess.run(["make", "all"], check=True)
		except subprocess.CalledProcessError:
			print(f"{RED}!!!! Fail to build {makefile} !!!!{RESET}")
			sys.exit(1)
		os.chdir(ROOT)


if __name__ == "__main__":
	main()