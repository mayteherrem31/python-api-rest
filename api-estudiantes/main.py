from fastapi import FastAPI

# Creamos una instancia de FastAPI.
# La variable app representa nuestra aplicación.
app = FastAPI()

# GET indica el método HTTP.
# "/" indica la ruta.
@app.get("/")
def inicio():
    return {"mensaje": "Hola, esta es mi primera API"}
    