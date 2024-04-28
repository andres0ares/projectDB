from pydantic import BaseModel
from typing import Union
from src.data.entities.cliente import Cliente
from src.data.entities.funcionario import Funcionario
from datetime import datetime

class Contrato(BaseModel):
    
    id: Union[int, None] = None
    cliente: Union[Cliente, None] = None
    funcionario: Union[Funcionario, None] = None
    data: datetime
    status: int # [0=pendente, 1=aprovado, 2=recusado]
