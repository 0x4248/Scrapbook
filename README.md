# Scrapbook

This repository is a collection of small systems experiments, one-off tools, hardware tests, and other work that doesn’t justify a standalone project. The layout is intentionally simple: each directory contains an isolated piece of work with its own notes and build files. Nothing here is polished; most of it exists to answer a question, verify a behavior, or document a quirk.

For projects that don’t fit cleanly into a tree (binaries, raw dumps, etc.), see the repository JunkDrawer.

![Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=0x4248&langs_count=50&exclude_repo=linux,busybox,0x4248.github.io,notebook&layout=compact&theme=dark)

*GitHub statistics are constrained; the language count is expanded here for reference.*

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

## ScrapExplorer

A simple browser for navigating this repository’s structure is available [here](https://0x4248.dev/Scrapbook/)

## License

Unless stated otherwise, code in this repository is released under the **GNU General Public License v3.0**. If a directory contains a LICENSE file, that license applies to the contents of that directory.

Additional acknowledgements can be found in `CREDITS.txt`.
