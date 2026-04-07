from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.core.config import settings

router = APIRouter()

templates = Jinja2Templates(directory="app/www/templates")

#páginas estáticas
routes = [
    {"name": "Home", "path": "/"},
    {"name": "API Docs", "path": "/docs"},
    {"name": "ReDoc", "path": "/redoc"},
]
context = {"title": settings.app_name,"content": settings.app_description,"routes": routes}
paginaInicial = templates.get_template("home.html").render(context)

about = {"title": "About","content": settings.app_about}
paginaAbout = templates.get_template("about.html").render(about)

@router.get("/", response_class=HTMLResponse,include_in_schema=False)
async def home():
    return paginaInicial

@router.get("/about", response_class=HTMLResponse,include_in_schema=False)
async def about():
    return paginaAbout