# Nexus

Primary repository containing all my projects, experiments, utilities, prototypes, and systems work — effectively a personal megarepo. This is the canonical source for everything I develop.

- Each subdirectory is self-contained, with its own build instructions, notes, or Makefiles.
- Nothing is guaranteed polished; most code exists to verify behavior, prototype ideas, or document quirks.
- Outputs that do not belong in a source tree (binaries, dumps, generated artifacts) live in the JunkDrawer repository.



## Repository Layout
```
arch/      Architecture-specific code and boot experiments  
systems/   OS-specific tools and tests  
usr/       User-space utilities  
lab/       Scratch work, prototypes, small experiments  
misc/      One-off fragments, language tests, and assorted files  
ext/       External libraries and third-party components  
doc/       Notes, references, and assorted documentation  
tools/     Build helpers and maintenance utilities  
```

Each subdirectory stands alone. Build methods vary please read the local `README` or `Makefile` where present.

## Atlas

A simple browser for navigating this repository’s structure is available [here](https://0x4248.dev/nexus/)

## Languages

*GitHub statistics are constrained; the language count is expanded here for reference.*

Language|files|blank %|comment %|code %
:-------|-------:|-------:|-------:|-------:
C|1170|11.35|17.74|70.91|
C/C++ Header|1582|8.67|17.66|73.67|
Bourne Shell|231|12.36|11.50|76.14|
Text|130|15.83|0.00|84.17|
XML|63|5.24|0.23|94.53|
Objective-C|37|16.44|11.25|72.32|
m4|15|9.71|1.25|89.04|
Python|45|22.45|31.88|45.66|
HTML|15|19.92|0.19|79.89|
C++|48|14.77|14.74|70.49|
Java|16|14.49|12.90|72.60|
CMake|16|8.59|22.24|69.17|
Assembly|26|6.10|17.26|76.63|
DOS Batch|42|1.85|0.36|97.79|
Markdown|36|26.54|0.00|73.46|
make|49|19.78|26.42|53.81|
Perl|5|12.87|18.41|68.72|
MSBuild script|3|0.00|0.00|100.00|
Glade|1|8.64|0.00|91.36|
yacc|1|13.62|2.93|83.46|
reStructuredText|1|26.99|10.11|62.90|
Visual Studio Solution|6|1.15|1.38|97.48|
Bourne Again Shell|7|13.30|20.37|66.33|
diff|6|9.43|25.82|64.75|
lex|1|11.27|3.38|85.35|
JavaScript|3|10.76|36.18|53.06|
NAnt script|1|24.42|0.00|75.58|
PowerShell|1|11.92|36.09|51.99|
CSS|2|13.39|0.00|86.61|
Fortran 90|7|17.18|42.75|40.08|
Metal|1|15.60|0.00|84.40|
Gradle|3|8.60|3.23|88.17|
Ant|1|18.28|16.13|65.59|
GLSL|4|20.39|31.07|48.54|
IDL|1|0.00|0.00|100.00|
Windows Resource File|2|9.76|9.76|80.49|
--------|--------|--------|--------|--------
SUM:|3597|11.57|15.96|72.47

## License

Unless stated otherwise, code in this repository is released under the **GNU General Public License v3.0**. If a directory contains a LICENSE file, that license applies to the contents of that directory.

Additional acknowledgements can be found in `CREDITS.txt`.
