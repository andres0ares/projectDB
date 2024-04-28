from src.data.entities.servico import Servico
from src.infra.Database import Database
from src.data.entities.login import Login
from fastapi import HTTPException
 
class ServicoDAO:
    def __init__(self):
        self.db =  Database()

    # a fazer
    def getAll(self):
         #retorna todos os itens da tabela carro
        query = "SELECT * FROM servico WHERE inativo = 0;"

        return [Servico.model_validate(car) for car in self.db.query(query)]
    
    def create(self, servico: Servico):
        servico.print()
        #cria um novo item da tabela servico
        query = f"INSERT INTO defaultdb.servico (nome, preco, descricao, img) VALUES ('{servico.nome}', '{servico.preco}', '{servico.descricao}', '{servico.img}');"

        return self.db.query(query)
    
    def update(self, servico: Servico):
        #atualiza o carro
        query = f"UPDATE servico SET preco = '{servico.preco}', descricao = '{servico.descricao}', nome = '{servico.nome}', img = '{servico.img}' WHERE id = {servico.id};"
        
        return self.db.query(query)
    
    def delete(self, id: int):
        #remove um carro pelo id
        query = f"UPDATE servico SET inativo = 1 WHERE id = {id};"
        #query = f"DELETE FROM carro WHERE id = {id};"

        return self.db.query(query)