from pydantic import BaseModel

class Carro(BaseModel):
    id: int | None = None
    modelo: str
    descricao: str | None = None
    nome: str
    img: str 

    def print(self):
        print(f"Carro: {self.nome}")