from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router=APIRouter()

@router.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')

@router.get('/', tags=['dashboard'])
def message():
    return {'message': 'bienvenido'}