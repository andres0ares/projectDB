from fastapi import APIRouter, Request
from src.data.control.ClienteDAO import ClienteDAO
from src.data.entities.cliente import Cliente

router = APIRouter()

handle = ClienteDAO()

# @router.get("/api/cars")
# async def getAll():
#     return handle.()

@router.post("/api/client")
async def create_item(client: Cliente):
    # Lê o conteúdo do corpo da requisição
    client.print()
    return True

# @router.put("/api/car")
# async def create_car(request: Request):
#     # Lê o conteúdo do corpo da requisição
#     body = await request.json()

#     carro = Carro(nome=body['nome'], modelo=body['modelo'], descricao=body['descricao'], img=body['img'], id=body['id'])
#     return handle.updateCarro(carro)

# @router.delete("/api/car/{id}")
# async def delete_car(id: int):
#     return handle.deleteCarro(id)

