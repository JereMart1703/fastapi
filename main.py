#Esta parte del codigo tiene que estar siempre al principio del archivo , en main.py
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
## Importar el modelo de Menu
from data.modelo.menu import Menu 
from data.database import database
from data.dao.dao_hospitales import DaoHospitales

app = FastAPI()

# Montar carpeta static para servir style.css
app.mount("/static", StaticFiles(directory="static"), name="static")

# Directorio de plantillas
templates = Jinja2Templates(directory="templates")

# Ejemplo de ruta
@app.get("/")
def read_root(request: Request):
    
    menu = {"home": True, "add": False}

    hospitales = DaoHospitales().get_all(database)  # Llamamos al método get_all de DaoHospitales
    return templates.TemplateResponse(
    "index.html",
    context={"request": request, "menu": menu, "hospitales": hospitales}
)


############################## DATABASE CONNECTION ##############################



