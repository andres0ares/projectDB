from pydantic import BaseModel
from typing import Union

class Carro(BaseModel):
    id: Union[int, None] = None
    modelo: str
    descricao: Union[str, None] = None
    nome: str
    img: str 

    def print(self):
        print(f"Carro: {self.nome}")