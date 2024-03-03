from fastapi import APIRouter, Request
from src.infra.Database import Database
from src.data.control.CarroViewModel import CarroViewModel
from src.data.entities.carro import Carro
router = APIRouter()

handle = CarroViewModel()

@router.get("/api/carros")
async def getAll():
    return handle.getCarros()

@router.post("/api/carro")
async def create_item(request: Request):
    # Lê o conteúdo do corpo da requisição
    body = await request.json()
    carro = Carro(nome=body['nome'], modelo=body['modelo'], descricao=body['descricao'], img=body['img'], id=None)
    return handle.createCarro(carro)