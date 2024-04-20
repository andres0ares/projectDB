from fastapi import APIRouter, Request
from src.data.control.FuncionarioDAO import FuncionarioDAO
from src.data.entities.funcionario import Funcionario
from src.data.entities.login import Login

router = APIRouter()

handle = FuncionarioDAO()

@router.get("/api/funcionario/all")
async def getall():
    return handle.getAll()

@router.post("/api/funcionario")
async def create(funcionario: Funcionario):
    return handle.create(funcionario)

@router.put("/api/funcionario")
async def update(funcionario: Funcionario):
    return handle.update(funcionario)
