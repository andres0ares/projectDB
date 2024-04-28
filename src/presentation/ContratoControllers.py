from fastapi import APIRouter, Request
from src.data.control.ContratoDAO import ContratoDAO
from src.data.entities.body import ContratoBody

router = APIRouter()

handle = ContratoDAO()

@router.post("/api/contrato")
async def create_item(client: ContratoBody):
    return handle.create(client)
