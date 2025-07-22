from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount the static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load HTML templates
templates = Jinja2Templates(directory="templates")

# Route for home page
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Mount the sub directory for exclusive page
app.mount("/sub", StaticFiles(directory="sub"), name="sub")

# Route for exclusive page
@app.get("/EXCLUSIVE.html", response_class=HTMLResponse)
async def read_exclusive(request: Request):
    return templates.TemplateResponse("EXCLUSIVE.html", {"request": request})

# ✅ Login page (GET)
@app.get("/login", response_class=HTMLResponse)
async def login_get(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


# ✅ Registration page (GET)
@app.get("/register.html", response_class=HTMLResponse)
async def register_get(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})