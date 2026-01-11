from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from core import page as p

router = APIRouter()

# ---- users DB (placeholder) ----

users = {
    "admin": {
        "password": "admin",
        "roles": ["admin", "user"],
        "email": "admin@orion",
        "telephone": "101",
    }
}

# ---- middleware ----

async def auth_middleware(request: Request, call_next):
    if request.url.path.startswith("/login"):
        return await call_next(request)

    user = request.cookies.get("user")
    if user in users:
        return await call_next(request)

    return RedirectResponse(url="/login", status_code=303)

# ---- routes ----

@router.get("/login")
async def login_page(request: Request):
    return p.form(
        request,
        title="LOGIN",
        action="/login",
        fields=[
            {"name": "username"},
            {"name": "password", "type": "password"},
        ],
        msg="Please login with your credentials.",
    )

@router.post("/login")
async def login_submit(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    user = users.get(username)
    if user and user["password"] == password:
        response = RedirectResponse(url="/", status_code=303)
        response.set_cookie("user", username, httponly=True)
        return response

    return p.form(
        request,
        title="LOGIN",
        action="/login",
        fields=[
            {"name": "username"},
            {"name": "password", "type": "password"},
        ],
        error="Invalid username or password.",
    )

@router.get("/logout")
async def logout():
    response = RedirectResponse("/login", status_code=303)
    response.delete_cookie("user")
    return response
