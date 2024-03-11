from pydantic import BaseModel
from typing import Union

class Servico(BaseModel):
    id: Union[int, None] = None
    nome: str
    img: str 
    descricao: Union[str, None] = None
    preco: float

    def print(self):
        print(f"servico: {self.nome}")