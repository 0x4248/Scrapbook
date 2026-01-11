from fastapi import Request
from core.registry import registry
from core.commands import Command
from core import page
import manpages.echo

def echo(request: Request, text: str = ""):
    if not text:
        return page.message(request, "ECHO", "No text provided")
    return page.message(request, "ECHO", text)

registry.register(Command(
    name="echo",
    handler=echo,
    summary="Echo back text",
    mode="both",
    form_fields=[
        {"name": "text", "type": "text"}
    ]
))
