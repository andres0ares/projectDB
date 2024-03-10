from src.data.entities.carro import Carro
from src.infra.Database import Database


class CarroDAO:
    def __init__(self):
        self.db =  Database()

    def getCarros(self) -> list[Carro]:
        return [Carro.parse_obj(car) for car in self.db.queryMany("SELECT * FROM carro;")]
    
    def createCarro(self, carro: Carro):
        query = f"INSERT INTO defaultdb.carro (nome, modelo, descricao, img) VALUES ('{carro.nome}', '{carro.modelo}', '{carro.descricao}', '{carro.img}');"
        return self.db.queryModify(query)
    
    # a fazer 
    def get(self, id: int):
        print(f"get carro por id: {id} ")
        return True
    
    # a fazer
    def updateCarro(self, carro: Carro):
        print(f"edit carro: {carro.id}", )
        return True
    
    # a fazer
    def deleteCarro(self, id: int):
        print(F"delete carro: {id}")
        return True
    # a fazer
    def searchByName(self, name: str):
        print(f"pesquisando: {name}...")
        return True