from pydantic import BaseModel
from typing import Union

class Cliente(BaseModel):
    id: Union[int, None] = None
    nome: str
    email: str
    senha: str

    def print(self):
        print(f"Cliente: {self.nome}, email: {self.email}, senha: {self.senha}")