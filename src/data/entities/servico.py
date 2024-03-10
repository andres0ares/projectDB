from pydantic import BaseModel

class Servico(BaseModel):
    id: int | None = None
    nome: str
    img: str 
    descricao: str | None = None
    preco: float

    def print(self):
        print(f"servico: {self.nome}")