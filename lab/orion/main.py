from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, RedirectResponse

from pages import command,about
from core import auth
from core import page as p


import commands.system.open

import commands.system.manual as manual
import commands.echo

app = FastAPI()



app.middleware("http")(auth.auth_middleware)

app.include_router(auth.router)
app.include_router(command.router)
app.include_router(about.router)
app.include_router(manual.router)

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
    uvicorn.run(app, host="0.0.0.0", port=8000)
