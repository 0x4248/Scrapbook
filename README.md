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

![Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=0x4248&langs_count=50&exclude_repo=linux,busybox,0x4248.github.io,notebook&layout=compact&theme=transparent)


## License

Unless stated otherwise, code in this repository is released under the **GNU General Public License v3.0**. If a directory contains a LICENSE file, that license applies to the contents of that directory.

Additional acknowledgements can be found in `CREDITS.txt`.
