from pydantic import BaseModel
from typing import Union

class Cliente(BaseModel):
    
    id: Union[int, None] = None
    nome: str
    email: str
    senha: str
    cidade: str
    e_flamengo: bool
    assiste_one_piece: bool

    def print(self):
        print(f"Cliente: {self.nome}, email: {self.email}, senha: {self.senha}, onePiece: {self.assiste_one_piece}, flam: {self.e_flamengo}, cidade: {self.cidade}")

    def getInfo(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "e_flamengo": self.e_flamengo,
            "assiste_one_piece": self.assiste_one_piece,
            "cidade": self.cidade
        }