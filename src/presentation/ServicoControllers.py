from fastapi import APIRouter, Request
from src.data.control.ServicoDAO import ServicoDAO
from src.data.entities.servico import Servico

router = APIRouter()

handle = ServicoDAO()

@router.get("/api/servico/all")
async def getAll():
    return handle.getAll()

@router.post("/api/servico")
async def post(servico: Servico):
    print('hehe', servico)
    return handle.create(servico)

@router.put("/api/servico")
async def put(servico: Servico):
    return handle.update(servico)

@router.delete("/api/servico/{id}")
async def delete_car(id: int):
    return handle.delete(id)