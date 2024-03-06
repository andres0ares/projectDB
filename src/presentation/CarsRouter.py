from fastapi import APIRouter, Request
from src.infra.Database import Database
from src.data.control.CarroViewModel import CarroViewModel
from src.data.entities.carro import Carro

router = APIRouter()

handle = CarroViewModel()

@router.get("/api/cars")
async def getAll():
    return handle.getCarros()

@router.post("/api/car")
async def create_item(request: Request):
    # Lê o conteúdo do corpo da requisição
    body = await request.json()

    carro = Carro(nome=body['nome'], modelo=body['modelo'], descricao=body['descricao'], img=body['img'], id=None)
    return handle.createCarro(carro)

@router.put("/api/car")
async def create_car(request: Request):
    # Lê o conteúdo do corpo da requisição
    body = await request.json()

    carro = Carro(nome=body['nome'], modelo=body['modelo'], descricao=body['descricao'], img=body['img'], id=body['id'])
    return handle.updateCarro(carro)

@router.delete("/api/car/{id}")
async def delete_car(id: int):
    return handle.deleteCarro(id)

