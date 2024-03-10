from fastapi import APIRouter, Request
from src.data.control.CarroDAO import CarroDAO
from src.data.entities.carro import Carro

router = APIRouter()

handle = CarroDAO()

@router.get("/api/cars")
async def getAll():
    return handle.getCarros()

@router.post("/api/car")
async def create_item(carro: Carro):
    return handle.createCarro(carro)

@router.put("/api/car")
async def create_car(carro: Carro):
    return handle.updateCarro(carro)

@router.delete("/api/car/{id}")
async def delete_car(id: int):
    return handle.deleteCarro(id)

