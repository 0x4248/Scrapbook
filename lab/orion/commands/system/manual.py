# Manual command man <name/alias> or ? <name/alias> or help <name/alias>
from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from core.registry import registry
from core.commands import Command
from core import page

from core.manual import manual_registry
from core.commands import Command

router = APIRouter()
@router.get("/man/{name}")
def manual_page_api(request: Request, name: str):
    return manual_page(request, name)

def manual_page(request: Request, name: str = ""):
    if name == "":
        # show forum
        return RedirectResponse(url="/forum/man")
    man = manual_registry.get(name)
    if not man:
        return page.message(
            request,
            "MANUAL",
            error=f"No manual page for: {name}"
        )
    
    return page.static(request, f"MANUAL PAGE FOR: {man.name.upper()}", html=f"""
    <h1 style="text-align: center; text-transform: uppercase;">{man.name}</h1>
<pre>{man.text}</pre>

<a href="javascript:history.back()" style="text-align:center">[ BACK ]</a>
                       """, buttons=page.with_nav(page.DEFAULT_NAV))

registry.register(Command(
    name="man",
    handler=manual_page,
    summary="Show manual page for command",
    mode="both",
    form_fields=[
        {"name": "name", "type": "text"},
    ],
))

### ALIASES ###

registry.register(Command(
    name="?",
    handler=manual_page,
    summary="Show manual page for command",
    mode="both",
    form_fields=[
        {"name": "name", "type": "text"},
    ],
))


registry.register(Command(
    name="help",
    handler=manual_page,
    summary="Show manual page for command",
    mode="both",
    form_fields=[
        {"name": "name", "type": "text"},
    ],
))
