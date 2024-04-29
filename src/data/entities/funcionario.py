from pydantic import BaseModel
from typing import Union

class Funcionario(BaseModel):
    id: Union[int, None] = None
    nome: str
    email: str
    senha: str

    def print(self):
        print(f"Funcionario: {self.nome}, email: {self.email}, senha: {self.senha}")

    def getInfo(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
        }