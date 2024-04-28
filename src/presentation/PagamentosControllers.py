from fastapi import APIRouter, Request
from src.data.control.PagamentoDAO import PagamentoDAO

router = APIRouter()

handle = PagamentoDAO()

@router.get("/api/pagamento")
async def getPagamentos():
    return handle.getPagamentos()
