# SPDX-License-Identifier: GPL-3.0
# Scraps
#
# Scrapbuild.py
# Makefile runner
#
# COPYRIGHT NOTICE
# Copyright (C) 2024 0x4248 and contributors
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the license is not changed.
#
# This software is free and open source. Licensed under the GNU general
# public license version 3.0 as published by the Free Software Foundation.

import sys
import subprocess
import os
import shutil

RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"
BLUE = "\033[34m"

def set_globals():
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
	return TYPE, MAKEFILES, ROOT

def print_status(current, makefile, maketype, MAKEFILES, TYPE):
	percent = current/len(MAKEFILES)*100
	percent = int(round(percent, 0))
	spaces = 3-len(str(percent))
	space_chars = " "*spaces
	if maketype == "make":
		print(f"[{space_chars}{percent}%]{BLUE} Running {TYPE} on makefile {makefile}{RESET}")
	elif maketype == "cmake":
		print(f"[{space_chars}{percent}%]{BLUE} Running {TYPE} on cmake {makefile}{RESET}")
	elif maketype == "bash":
		print(f"[{space_chars}{percent}%]{BLUE} Running {TYPE} on bash {makefile}{RESET}")

def main():
	print(f"{BLUE}STARTING SCRAPBUILD{RESET}")

	TYPE, MAKEFILES, ROOT = set_globals()

	current = 0
	for makefile in MAKEFILES:
		maketype = "make"

		if makefile.startswith("!"):
			maketype = "cmake"
			makefile = makefile[1:]
		
		if makefile.startswith("@"):
			maketype = "bash"
			makefile = makefile[1:]

		if maketype == "make":
			os.chdir(os.path.dirname(makefile))
		elif maketype == "cmake":
			os.chdir(makefile)
		elif maketype == "bash":
			makefile = os.path.join(ROOT, makefile)
			os.chdir(os.path.dirname(makefile))

		print_status(current, makefile, maketype, MAKEFILES, TYPE)
		current += 1

		# Try to run the makefile and if it fails stop
		try:
			if TYPE == "clean":
				if maketype == "make":
					subprocess.run(["make", "clean"], check=True)
				elif maketype == "cmake":
					subprocess.run(["mkdir", "-p", "build"], check=True)
					os.chdir("build")
					subprocess.run(["cmake", ".."], check=True)
					subprocess.run(["make", "clean"], check=True)
					os.chdir("..")
					shutil.rmtree("build")
				elif maketype == "bash":
					subprocess.run(["bash", makefile, "clean"], check=True)
			elif TYPE == "all":
				if maketype == "make":
					subprocess.run(["make", "all"], check=True)
				elif maketype == "cmake":
					if os.path.isdir("build"):
						shutil.rmtree("build")
					subprocess.run(["mkdir", "-p", "build"], check=True)
					os.chdir("build")
					subprocess.run(["cmake", ".."], check=True)
					subprocess.run(["make", "all"], check=True)
				elif maketype == "bash":
					subprocess.run(["bash", makefile, "all"], check=True)
		except subprocess.CalledProcessError:
			print(f"{RED}!!!! Fail to build {makefile} !!!!{RESET}")
			sys.exit(1)

		os.chdir(ROOT)


if __name__ == "__main__":
	main()
