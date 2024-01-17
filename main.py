from fastapi import FastAPI, Request, Form, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pydantic import EmailStr, ValidationError
from utils.email import send_email
from model import Formulario



app = FastAPI()
# new version
app.mount("{{url_for('assets', path='", StaticFiles(directory="assets"), name="assets")
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

@app.get("/1", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("1.html", {"request": request})

@app.get("/1english", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("1english.html", {"request": request})

@app.get("/2", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("2.html", {"request": request})

@app.get("/2english", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("2english.html", {"request": request})

@app.get("/3", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("3.html", {"request": request})

@app.get("/3english", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("3english.html", {"request": request})

@app.get("/blogenglish", tags=["inicio"])
async def root(request: Request):
    return templates.TemplateResponse("blogenglish.html", {"request": request})

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

@app.post("/sendform", tags=["contacto"])
async def form(request : Request, name: str = Form(...), age: int = Form(...), 
               email: EmailStr = Form(...), person_number: int = Form(...), adult_number: int = Form(...),
               children_number: int = Form(...), destiny: str = Form(...), duration: int = Form(...),
               start_date: str = Form(...), end_date:str = Form(...), experiences:str = Form(...)
               ):
    
    try:   
        formulario = Formulario(**{"name": name, "age":age, "email":email, 
                                   "person_number": person_number, "adult_number": adult_number,
                                    "children_number": children_number, "destiny": destiny, 
                                    "duration": duration, "start_date": start_date, 
                                    "end_date": end_date, "experiences": experiences})

    except ValidationError as e:
        return templates.TemplateResponse("error.html", {"request": request, "errors": e.errors()})
    
    destinatario = "info@arttraces.net"
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
    if result == "Correo enviado exitosamente":
        return templates.TemplateResponse("warning.html", {"request": request})
    else: 
        return JSONResponse("Error al enviar el correo", status_code=400)

@app.post("/sendformenglish", tags=["contacto"])
async def form(request : Request, name: str = Form(...), age: int = Form(...), 
               email: EmailStr = Form(...), person_number: int = Form(...), adult_number: int = Form(...),
               children_number: int = Form(...), destiny: str = Form(...), duration: int = Form(...),
               start_date: str = Form(...), end_date:str = Form(...), experiences:str = Form(...)
               ):
    
    try:   
        formulario = Formulario(**{"name": name, "age":age, "email":email, 
                                   "person_number": person_number, "adult_number": adult_number,
                                    "children_number": children_number, "destiny": destiny, 
                                    "duration": duration, "start_date": start_date, 
                                    "end_date": end_date, "experiences": experiences})
 
    except ValidationError as e:
        return templates.TemplateResponse("errorenglish.html", {"request": request, "errors": e.errors()})
    
    destinatario = "info@arttraces.net"
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
    if result == "Correo enviado exitosamente":
        return templates.TemplateResponse("warningenglish.html", {"request": request})
    else: 
        return JSONResponse("Error al enviar el correo", status_code=400)
    
@app.get("/sitemap.xml", tags=["google"])
async def google(request: Request):
    data = """<?xml version="1.0" encoding="UTF-8"?> 
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"> 
    <url>
      <loc>https://www.arttraces.net/</loc>
      <priority>0.6</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/destinocuba</loc>
      <priority>0.2</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/destinomexico</loc>
      <priority>0.7</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/indexgaleria</loc>
      <priority>0.5</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/contacto</loc>
      <priority>1.0</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/main</loc>
      <priority>0.5</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/destinocubaenglish</loc>
      <priority>0.5</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/artecuba</loc>
      <priority>0.5</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/arquitecturacuba</loc>
      <priority>0.6</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/fotografiacuba</loc>
      <priority>0.5</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/religioncuba</loc>
      <priority>0.6</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/shoppingcuba</loc>
      <priority>0.4</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/destinomexicoenglish</loc>
      <priority>0.2</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/arteyucatan</loc>
      <priority>0.1</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/arquitecturayucatan</loc>
      <priority>0.6</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/bienestaryucatan</loc>
      <priority>0.2</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/cenotesyucatan</loc>
      <priority>0.3</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/haciendasyucatan</loc>
      <priority>0.1</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/gastronomiayucatan</loc>
      <priority>0.7</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/vidanocturnayucatan</loc>
      <priority>0.7</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/ecoturismoyucatan</loc>
      <priority>0.9</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/peopleyucatan</loc>
      <priority>0.6</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc></loc>
      <priority>0.1</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/contactoenglish</loc>
      <priority>1.0</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/indexgaleriaenglish</loc>
      <priority>0.7</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/artecubaenglish</loc>
      <priority>1.0</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/arquitecturacubaenglish</loc>
      <priority>0.5</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/fotografiacubaenglish</loc>
      <priority>0.4</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/religioncubaenglish</loc>
      <priority>0.5</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/shoppingcubaenglish</loc>
      <priority>0.5</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net{{url_for('assets', path='/galeria/indexgaleria</loc>
      <priority>0.4</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/arteyucatanenglish</loc>
      <priority>0.4</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/arquitecturayucatanenglish</loc>
      <priority>0.7</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/bienestaryucatanenglish</loc>
      <priority>0.7</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/cenotesyucatanenglish</loc>
      <priority>0.7</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/haciendasyucatanenglish</loc>
      <priority>0.5</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/gastronomiayucatanenglish</loc>
      <priority>0.8</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/vidanocturnayucatanenglish</loc>
      <priority>1.0</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/ecoturismoyucatanenglish</loc>
      <priority>0.9</priority>
      <changefreq>weekly</changefreq>
    </url>
    <url>
      <loc>https://www.arttraces.net/peopleyucatanenglish</loc>
      <priority>0.2</priority>
      <changefreq>weekly</changefreq>
    </url>
    </urlset>"""

    return Response(content=data, media_type="application/xml")