from src.data.entities.carro import Carro
from src.infra.Database import Database


class CarroDAO:
    def __init__(self):
        self.db =  Database()

    
    def getAll(self) -> list[Carro]:
        #retorna todos os itens da tabela carro
        query = "SELECT * FROM carro WHERE inativo = 0;"

        return [Carro.model_validate(car) for car in self.db.query(query)]
    
    def create(self, carro: Carro):
        #cria um novo item da tabela carro
        query = f"INSERT INTO defaultdb.carro (nome, modelo, descricao, img) VALUES ('{carro.nome}', '{carro.modelo}', '{carro.descricao}', '{carro.img}');"

        return self.db.query(query)
    
    def get(self, id: int):
        #busca um item na tabela carro poelo id
        query = f"SELECT * FROM carro WHERE id = {id};" 

        return self.db.query(query)
    
    def update(self, carro: Carro):
        #atualiza o carro
        query = f"UPDATE carro SET modelo = '{carro.modelo}', descricao = '{carro.descricao}', nome = '{carro.nome}', img = '{carro.img}' WHERE id = {carro.id};"
        
        return self.db.query(query)
    
    def delete(self, id: int):
        #remove um carro pelo id
        query = f"UPDATE carro SET inativo = 1 WHERE id = {id};"
        #query = f"DELETE FROM carro WHERE id = {id};"

        return self.db.query(query)
    
    def searchByName(self, name: str):
        #busca os carros que possuem a substring name na propriedade nome.
        query = f"SELECT * FROM carro WHERE nome LIKE '%{name}%';"
       
        return self.db.query(query)