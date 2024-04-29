from fastapi import APIRouter, Request
from src.data.control.PagamentoDAO import PagamentoDAO
from src.data.entities.body import Aprove

router = APIRouter()

handle = PagamentoDAO()

@router.get("/api/pagamento")
async def getPagamentos():
    return handle.getPagamentos()

@router.put("/api/pagamento/aprove")
async def changeStatus(body: Aprove):
    return handle.updateAprove(body)