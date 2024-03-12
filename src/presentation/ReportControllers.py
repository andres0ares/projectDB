from fastapi import APIRouter, Request
from src.data.control.RelatorioViewModel import Relatorio

router = APIRouter()
handle = Relatorio()

@router.get("/api/report/list")
async def _getList():
    return handle.getList()

@router.get("/api/report/{option}")
async def _gerReport(option: int):
    return handle.get(option)


