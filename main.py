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

@app.get("/main", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("indexenglish.html", {"request": request})

@app.get("/destinocuba", tags=["cuba"])
async def root(request: Request):
    return templates.TemplateResponse("destinocuba.html", {"request": request})

@app.get("/destinocubaenglish", tags=["cuba"])
async def root(request: Request):
    return templates.TemplateResponse("destinocubaenglish.html", {"request": request})

@app.get("/destinomexico", tags=["mexico"])
async def root(request: Request):
    return templates.TemplateResponse("destinomexico.html", {"request": request})

@app.get("/destinomexicoenglish", tags=["mexico"])
async def root(request: Request):
    return templates.TemplateResponse("destinomexicoenglish.html", {"request": request})


@app.get("/contacto", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("contacto.html", {"request": request})

@app.get("/contactoenglish", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("contactoenglish.html", {"request": request})

@app.get("/arquitecturacuba", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("arquitecturacuba.html", {"request": request})

@app.get("/arquitecturacubaenglish", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("arquitecturacubaenglish.html", {"request": request})

@app.get("/arquitecturayucatan", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("arquitecturayucatan.html", {"request": request})

@app.get("/arquitecturayucatanenglish", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("arquitecturayucatanenglish.html", {"request": request})

@app.get("/artecuba", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("artecuba.html", {"request": request})

@app.get("/artecubaenglish", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("artecubaenglish.html", {"request": request})

@app.get("/arteyucatan", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("arteyucatan.html", {"request": request})

@app.get("/arteyucatanenglish", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("arteyucatanenglish.html", {"request": request})

@app.get("/bienestaryucatan", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("bienestaryucatan.html", {"request": request})

@app.get("/bienestaryucatanenglish", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("bienestaryucatanenglish.html", {"request": request})

@app.get("/blog", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("blog.html", {"request": request})

@app.get("/cenotesyucatan", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("cenotesyucatan.html", {"request": request})

@app.get("/cenotesyucatanenglish", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("cenotesyucatanenglish.html", {"request": request})

@app.get("/ecoturismoyucatan", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("ecoturismoyucatan.html", {"request": request})

@app.get("/ecoturismoyucatanenglish", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("ecoturismoyucatanenglish.html", {"request": request})

@app.get("/fotografiacuba", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("fotografiacuba.html", {"request": request})

@app.get("/fotografiacubaenglish", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("fotografiacubaenglish.html", {"request": request})

@app.get("/gastronomiayucatan", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("gastronomiayucatan.html", {"request": request})

@app.get("/gastronomiayucatanenglish", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("gastronomiayucatanenglish.html", {"request": request})

@app.get("/haciendasyucatan", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("haciendasyucatan.html", {"request": request})

@app.get("/haciendasyucatanenglish", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("haciendasyucatanenglish.html", {"request": request})

@app.get("/indexgaleria", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("indexgaleria.html", {"request": request})

@app.get("/indexgaleriaenglish", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("indexgaleriaenglish.html", {"request": request})

@app.get("/peopleyucatan", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("peopleyucatan.html", {"request": request})

@app.get("/peopleyucatanenglish", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("peopleyucatanenglish.html", {"request": request})

@app.get("/religioncuba", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("religioncuba.html", {"request": request})

@app.get("/religioncubaenglish", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("religioncubaenglish.html", {"request": request})

@app.get("/shoppingcuba", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("shoppingcuba.html", {"request": request})

@app.get("/shoppingcubaenglish", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("shoppingcubaenglish.html", {"request": request})

@app.get("/vidanocturnayucatan", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("vidanocturnayucatan.html", {"request": request})

@app.get("/vidanocturnayucatanenglish", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("vidanocturnayucatanenglish.html", {"request": request})


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
