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


# Imports we need
import sys
import subprocess
import os


# Just some ANSI escape codes for colors
RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"
BLUE = "\033[34m"

def main():
	print(f"{BLUE}STARTING SCRAPBUILD{RESET}")
	# First we need to check if the caller has given the correct arguments
	# TYPE - This should contain the type of build we are doing. Either "clean" 
	# or "all". "clean" should tell all the sub-makefiles to clean up and "all"
	# should tell all the sub-makefiles to build.
	# MAKEFILES - This should contain the list of makefiles we are going to run.
	# For example ABC/Makefile, XYZ/Makefile etc.

	TYPE = sys.argv[1]
	MAKEFILES = sys.argv[2:]
	
	# Prechecks
	if MAKEFILES == []:
		print("No makefiles specified.")
		# Exit with error code 1 to indicate an error
		sys.exit(1)
	
	# This should be the current directory of the main makefile
	ROOT = os.getcwd()
	if TYPE not in ["clean", "all"]:
		print("Invalid type. Use 'clean' or 'all'.")
		sys.exit(1)
	if TYPE == "clean":
		print(f"{BLUE}Cleaning makefiles.{RESET}")
	elif TYPE == "all":
		print(f"{BLUE}Building makefiles.{RESET}")
	
	# Current counts the current index of the makefile we are building
	current = 0
	for makefile in MAKEFILES:
		# First we need to change the directory to the directory of the makefile
		# so that when the makefile calls a relative path, it will work.
		os.chdir(os.path.dirname(makefile))

		# Now we can run the makefile
		print(f"[{GREEN}{current/len(MAKEFILES)*100}%{RESET}] {GREEN}{makefile}{RESET}")
		current += 1

		# Try to run the makefile and if it fails stop
		try:
			if TYPE == "clean":
				subprocess.run(["make", "clean"], check=True)
			elif TYPE == "all":
				subprocess.run(["make", "all"], check=True)
		except subprocess.CalledProcessError:
			print(f"{RED}!!!! Fail to build {makefile} !!!!{RESET}")
			sys.exit(1)

		# Change back to the root directory
		os.chdir(ROOT)


if __name__ == "__main__":
	main()
