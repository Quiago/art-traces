from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pydantic import EmailStr
from utils.email import send_email




app = FastAPI()
app.mount("/assets", StaticFiles(directory="assets"), name="assets")
templates = Jinja2Templates(directory="templates")



@app.get("/", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/destinocuba", tags=["cuba"])
async def root(request: Request):
    return templates.TemplateResponse("destinocuba.html", {"request": request})

@app.get("/destinomexico", tags=["mexico"])
async def root(request: Request):
    return templates.TemplateResponse("destinomexico.html", {"request": request})

@app.get("/contacto", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("contacto.html", {"request": request})

@app.get("/blogs/{id_blog}", tags=["blogs"])
async def root(request: Request, id_blog:str):


    h1 = "Este blog es sobre Mexico y sus tallas interesantes quiero ver si saleeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
    h2 = "Este es un blog sobre Cuba y sus tallas interseantes quiero ver si funcionaaaaaaaaaaaaaaaa"
    content = ""
    if id_blog == "1":
        content = h1
    if id_blog == "2":
        content = h2
    print(content)
    return templates.TemplateResponse("blog.html", {"request": request, "content": content})

@app.post("/sendform", tags=["inicio"])
async def form(name: str = Form(min_length=1, max_length=100), age: int = Form(ge=0, le=100), 
               email: EmailStr = Form(...), person_number: int = Form(ge=0, le=50), adult_number: int = Form(ge=0, le=50),
               children_number: int = Form(ge=0, le=50), destiny: str = Form(min_length=1, max_length=100), duration: int = Form(ge=0, le=50),
               start_date: str = Form(...), end_date:str = Form(...), experiences:str = Form(min_length=1, max_length=300),
               ):
    
    datos = { "name" : name, 
            "age": age, 
               "email": email, 
               "person_number": person_number ,
               "adult_number": adult_number,
               "children_number": children_number, 
               "destiny": destiny,
               "duration": duration,
               "start_date": start_date, 
               "end_date": end_date, 
               "experiences": experiences
               }

    destinatario = "danielsierraperera07@gmail.com"
    asunto = "Art Traces Reservation"
    mensaje = f"""Los datos de la reservación son los siguientes:
Nombre: {name}
Edad: {age}
Correo Electrónico: {email}
Cantidad de personas: {person_number}
Cantidad de adultos: {adult_number}
Cantidad de menores de edad: {children_number}
Destino: {destiny}
Duración: {duration}
Fecha de Ida: {start_date}
Fecha de Retorno: {end_date}
Intereses": {experiences}"""
    result = send_email(destinatario, asunto, mensaje)
    return JSONResponse(content=result, status_code=201)
