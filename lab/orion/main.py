from fastapi import FastAPI, Request
from fastapi.responses import FileResponse

from core.logbridge import logBridge
from pages import command, about, console
from core import auth, console
from core import page as p

import commands.system.open
import commands.system.manual as manual
import commands.echo
import logging

handler = logBridge(console.logger)
handler.setFormatter(logging.Formatter("%(message)s"))

root = logging.getLogger()
root.handlers.clear()
root.addHandler(handler)
root.setLevel(logging.DEBUG)

for name in (
    "uvicorn",
    "uvicorn.error",
    "uvicorn.access",
    "fastapi",
):
    log = logging.getLogger(name)
    log.handlers.clear()
    log.addHandler(handler)
    log.propagate = False


app = FastAPI()

console.logger.info(m="Starting Orion Web Application")

app.middleware("http")(auth.auth_middleware)

app.include_router(auth.router)
app.include_router(command.router)
app.include_router(about.router)
app.include_router(manual.router)

console.logger.info(m=app.router.routes)

@app.exception_handler(404)
async def not_found(request: Request, exc):
    return p.static(
        request,
        "404 NOT FOUND",
        "<pre class='error'>404 NOT FOUND</pre>"
        "<a href='javascript:history.back()'>[ BACK ]</a>",
    )

@app.get("/favicon.ico")
async def favicon():
    return FileResponse("./static/mascot.ico")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_config=None,
        access_log=True,
    )
