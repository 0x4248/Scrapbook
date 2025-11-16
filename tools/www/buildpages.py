#!/usr/bin/env python3
import html
import os
import shutil

try:
    import markdown
except ImportError:
    os.system("pip3 install markdown")

from markdown.core import Markdown

ROOT = os.getcwd()
SRC_DIR = ROOT
OUT_DIR = os.path.join(ROOT, "pages")

IGNORE_DIRS = [".git", "build", "data", "tmp", "bin", "__pycache__", "pages"]

TEMPLATE = """<!doctype html>
<html>
    <head>
        <title>{title}</title>
        <link rel="stylesheet" href="/misc/www/css/basic_mono.css"/>
        <link rel="stylesheet" href="/misc/www/css/ScrapExplorer/main.css"/>

        <style>
        .ln {{
            display: inline-block;
            opacity: 0.5;
            margin-right: 10px;
            color: #888;
            text-align: right;
            width: 3em;
            user-select: none;
        }}
        body.show-lines .ln {{
            display: inline-block;
        }}
        body.hide-lines .ln {{
            display: none;
        }}
        </style>

        <script>
        function toggleLineNumbers() {{
            document.body.classList.toggle("show-lines");
            document.body.classList.toggle("hide-lines");
        }}
        </script>
    </head>
    <body class="show-lines">
        <pre>
<h1>{title}</h1>
{breadcrumbs}
{stats}{toolbar}
{separator}
{content}
<div class="separator">[{endtag}]</div>
(C) 2025 0x4248
(C) 2025 4248 Media and 4248 Systems, All part of 0x4248
See LICENCE files for more information
        </pre>
    </body>
</html>
"""


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def write_file(path, content):
    ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def compute_breadcrumbs(rel_path):
    if not rel_path:
        return "Home"

    parts = rel_path.split("/")
    crumbs = ['<a href="/index.html">Home</a>']

    accum = ""
    for p in parts:
        accum = os.path.join(accum, p)
        crumbs.append(f'<a href="/{accum}/index.html">{p}</a>')

    return " / ".join(crumbs)


def is_binary(filepath, sample_size=2048):
    try:
        with open(filepath, "rb") as f:
            chunk = f.read(sample_size)
            if not chunk:
                return False
            if b"\0" in chunk:
                return True

            try:
                chunk.decode("utf-8")
                return False
            except UnicodeDecodeError:
                return True
    except Exception:
        return True


def make_file_page(src_path, out_path_rel):
    filename = os.path.basename(src_path)
    rel_path_dir = os.path.dirname(out_path_rel)
    breadcrumbs = compute_breadcrumbs(rel_path_dir)
    filesize = os.path.getsize(src_path)

    repo = "0x4248/Scrapbook"

    repo_path = out_path_rel.replace(".html", "")
    github_url = f"https://github.com/{repo}/blob/main/{repo_path}"
    github_raw = f"https://raw.githubusercontent.com/{repo}/main/{repo_path}"

    if is_binary(src_path):
        stats = f"Size: {filesize} bytes\n"
        toolbar = (
            f'<a href="{filename}" download>[Download file]</a> '
            f'<a href="{github_url}">[Show on GitHub]</a> '
            f'<a href="{github_raw}">[Raw]</a> '
        )
        content = (
            "<p style='text-align:center;'>Binary file cannot be displayed.</p>\n"
            f'<a style="text-align:center;display:block;" href="{filename}" download>[Download]</a>\n'
        )
    else:
        with open(src_path, "r", encoding="utf-8", errors="replace") as f:
            text = f.read()

        escaped = html.escape(text)
        lines = escaped.split("\n")

        numbered = "\n".join(
            f'<span class="ln">{i + 1}</span>{line}' for i, line in enumerate(lines)
        )

        stats = f"Lines: {text.count('\\n') + 1} | Size: {filesize} bytes\n"
        toolbar = (
            f'<a href="{filename}" download>[Download file]</a> '
            f'<a href="#" onclick="toggleLineNumbers();return false;">[Toggle line #]</a> '
            f'<a href="{github_url}">[Show on GitHub]</a> '
            f'<a href="{github_raw}">[Raw]</a> '
        )
        content = numbered

    page = TEMPLATE.format(
        title="ScrapExplorer - " + filename,
        breadcrumbs=breadcrumbs,
        stats=stats,
        toolbar=toolbar,
        separator='<div class="separator">[FILE BEGIN]</div>',
        endtag="FILE END",
        content=content,
    )

    write_file(os.path.join(OUT_DIR, out_path_rel), page)


def make_directory_index(dir_path, rel_path):
    entries = sorted(os.listdir(dir_path))

    intro = ""

    readme_paths = [
        os.path.join(dir_path, "README.txt"),
        os.path.join(dir_path, "README"),
        os.path.join(dir_path, "README.html"),
        os.path.join(dir_path, "README.md"),
    ]
    for readme_path in readme_paths:
        if rel_path == "":
            with open("pages/README.txt", "r", encoding="utf-8", errors="replace") as f:
                intro_text = f.read()
                intro = intro_text + "\n\n<hr>\n\n"
        elif os.path.exists(readme_path):
            with open(readme_path, "r", encoding="utf-8", errors="replace") as f:
                if readme_path.endswith(".html"):
                    intro_text = f.read()
                elif readme_path.endswith(".md"):
                    intro_text = markdown.markdown(f.read())
                else:
                    intro_text = html.escape(f.read())
                intro = intro_text + "\n\n<hr>\n\n"

    lines = []
    if rel_path != "":
        lines.append('* <a href="../">../</a>')

    for name in entries:
        if any(name.startswith(d) for d in IGNORE_DIRS):
            continue

        full = os.path.join(dir_path, name)
        if os.path.isdir(full):
            lines.append(f'* <a href="{name}/index.html">{name}/</a>')
        else:
            lines.append(f'* <a href="{name}.html">{name}</a>')

    content = intro + "\n".join(lines)

    breadcrumbs = compute_breadcrumbs(rel_path)
    title_path = "Home" if rel_path == "" else rel_path

    page = TEMPLATE.format(
        title="ScrapExplorer - " + title_path,
        breadcrumbs=breadcrumbs,
        stats="",
        toolbar="",
        separator='<div class="separator">[DIR BEGIN]</div>',
        endtag="DIR END",
        content=content,
    )

    write_file(os.path.join(OUT_DIR, rel_path, "index.html"), page)


def copy_raw_file(src_path, rel_path):
    dest = os.path.join(OUT_DIR, rel_path)
    ensure_dir(os.path.dirname(dest))
    shutil.copy2(src_path, dest)


def main():
    if os.path.exists(OUT_DIR):
        shutil.rmtree(OUT_DIR)
    ensure_dir(OUT_DIR)
    shutil.copy("doc/ScrapExplorer/welcome.txt", "pages/README.txt")

    for dirpath, dirs, files in os.walk(SRC_DIR):
        if dirpath.startswith(OUT_DIR):
            continue

        rel = os.path.relpath(dirpath, SRC_DIR)
        if rel == ".":
            rel = ""

        make_directory_index(dirpath, rel)

        for file in files:
            if file.startswith(".") or "buildpages.py" in file:
                continue

            src_file = os.path.join(dirpath, file)
            rel_file = os.path.join(rel, file)

            copy_raw_file(src_file, rel_file)
            make_file_page(src_file, rel_file + ".html")


if __name__ == "__main__":
    main()
