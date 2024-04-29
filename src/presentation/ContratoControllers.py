from fastapi import APIRouter, Request
from src.data.control.ContratoDAO import ContratoDAO
from src.data.entities.body import ContratoBody
from src.data.entities.body import Id
from src.data.control.AtendimentoDAO import AtendimentoDAO

router = APIRouter()
handle = ContratoDAO()
handle2 = AtendimentoDAO()

@router.post("/api/contrato")
async def create_item(client: ContratoBody):
    return handle.create(client)

@router.get("/api/contrato/{id}")
async def getAllByclient(id: int):
    return handle.getAllByClient(id)

@router.get("/api/contrato/status/{status}")
async def getAllByclient(status: int):
    return handle.getAllByStatus(status)

@router.get("/api/contrato/funcionario/{funcionario_id}")
async def getAllByclient(funcionario_id: int):
    return handle.getAllByStaff(funcionario_id)

@router.put("/api/contrato/status")
async def changeStatus(body: Id):
    return handle.updateStatus(body)

@router.get("/api/atendimentos/format")
async def getAtendimentos():
    return handle2.getAtendimentosFormat()