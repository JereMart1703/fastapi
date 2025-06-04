from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Montar carpeta static para servir style.css
app.mount("/static", StaticFiles(directory="static"), name="static")

# Directorio de plantillas
templates = Jinja2Templates(directory="templates")

# Ejemplo de ruta
@app.get("/")
def read_root(request: Request):
    menu = {"home": True, "add": True}
    return templates.TemplateResponse("base.html", {"request": request, "menu": menu})
