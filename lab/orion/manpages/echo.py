from core import manual

manual.manual_registry.register(
    name="echo",
    text="""
DESCRIPTION:
    Echo back the provided text.

USAGE:
    echo <text>

EXAMPLE:
    $ echo Hello, World!
    Hello, World!

ALIASES:
    none
"""
)