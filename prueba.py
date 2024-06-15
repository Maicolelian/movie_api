from fastapi import FastAPI

app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"


@app.get('/consultar_usuarios')
def consultar_usuarios():
    return "Bienvenido Maicoll..."

@app.post('/insertar_usuarios')
def insertar_usuarios():
    return "usuario insertado"

@app.put('/actualizar_usuarios')
def actualizar_usuarios():
    return "usuario actualizado..."

@app.delete('/eliminar_usuarios')
def eliminar_usuarios():
    return "usuario eliminado..."

@app.patch('/subir_usuarios')
def subir_usuarios():
    return "subiendo usuario..."

