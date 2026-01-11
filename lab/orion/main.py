from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from pages import command
from core import auth
from core import page as p


import commands.system.open
# import commands.testing.demo
import commands.echo

app = FastAPI()



app.middleware("http")(auth.auth_middleware)

app.include_router(auth.router)
app.include_router(command.router)


@app.exception_handler(404)
async def not_found(request: Request, exc):
    return p.static(
        request,
        "404 NOT FOUND",
        "<pre class='error'>404 NOT FOUND</pre>"
        "<a href='javascript:history.back()'>[ BACK ]</a>",
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
