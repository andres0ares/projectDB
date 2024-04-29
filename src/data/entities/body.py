from pydantic import BaseModel
from typing import Union
from src.data.entities.carro import Carro
from src.data.entities.servico import Servico
from datetime import datetime

class Cliente(BaseModel):
    
    id: Union[int, None] = None
    nome: str
    email: str
    cidade: str
    e_flamengo: bool
    assiste_one_piece: bool

class Atendimento(BaseModel):
    
    carro: Carro
    servico: Servico
    placa: str
    agendamento: datetime

class ContratoBody(BaseModel):
    cliente: Cliente
    atendimentos: list[Atendimento]
    forma_pagamento: int

class Id(BaseModel):
    contrato_id: int
    funcionario_id: int

class Aprove(BaseModel):
    contrato_id: int
    forma_pagamento: int