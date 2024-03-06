from src.data.entities.carro import Carro
from src.infra.Database import Database


class CarroViewModel:
    def __init__(self):
        self.db =  Database()

    def getCarros(self) -> list[Carro]:
        query = "SELECT * FROM carro;"
        return self.db.queryMany(query)
    
    def createCarro(self, carro: Carro):
        query = f"INSERT INTO defaultdb.carro (nome, modelo, descricao, img) VALUES ('{carro.nome}', '{carro.modelo}', '{carro.descricao}', '{carro.img}');"
        print(query)
        return self.db.queryModify(query)
    
    #a fazer
    def updateCarro(self, carro: Carro):
        print('edit carro: ', carro.id)
        return True
    #a fazer
    def deleteCarro(self, id: int):
        print('delete carro: ', id)
        return True