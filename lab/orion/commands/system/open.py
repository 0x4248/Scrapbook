from fastapi import Request
from fastapi.responses import RedirectResponse
from core.registry import registry
from core.commands import Command
from core import page


def open_page(request: Request, name: str = ""):
    if not name:
        return page.message(
            request,
            "OPEN",
            "usage: open <page>"
        )

    cmd = registry.get(name)
    if not cmd or not cmd.supports_ui():
        return page.message(
            request,
            "OPEN",
            f"No UI page for: {name}"
        )

    return RedirectResponse(f"/command/{name}", status_code=303)

registry.register(Command(
    name="open",
    handler=open_page,
    summary="Open a UI page",
    mode="cli",
))
