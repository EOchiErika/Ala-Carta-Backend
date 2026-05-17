from fastapi import FastAPI #Trae la erramienta principal de fastapi

app = FastAPI() #crea la app

@app.get("/") #lo que se va a mostrar si se ingresa a la raiz del sistema
def root():
    return {"message": "Mi primer proyecto grande"}