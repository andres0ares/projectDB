from pydantic import BaseModel
from typing import Union
from src.data.entities.servico import Servico
from src.data.entities.contrato import Contrato
from src.data.entities.carro import Carro
from datetime import datetime

class Atendimento(BaseModel):
    
    id: Union[int, None] = None
    data_agendada: datetime
    cancelado: bool
    placa: str
    status: int # [0=pendente, 1=aprovado, 2=recusado]
    carro: Union[Carro, None] = None
    servico: Union[Servico, None] = None
    contrato: Union[Contrato, None] = None
