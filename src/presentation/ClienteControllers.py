from fastapi import APIRouter, Request
from src.data.control.ClienteDAO import ClienteDAO
from src.data.entities.cliente import Cliente
from src.data.entities.login import Login

router = APIRouter()

handle = ClienteDAO()

@router.post("/api/client")
async def create_item(client: Cliente):
    return handle.create(client)

@router.post("/api/client/login")
async def create_item(login: Login):
    return handle.login(login)

