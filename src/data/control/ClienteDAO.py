from src.infra.Database import Database
from src.data.entities.cliente import Cliente
from src.data.entities.login import Login
from fastapi import HTTPException
 
class ClienteDAO:
    def __init__(self):
        self.db =  Database()
    
    def create(self, cliente: Cliente):
        query = f"INSERT INTO cliente (nome, email, senha, cidade, e_flamengo, assiste_one_piece ) VALUES ('{cliente.nome}', '{cliente.email}', '{cliente.senha}', '{cliente.cidade}', {1 if cliente.e_flamengo else 0}, {1 if cliente.assiste_one_piece else 0});"
        try:  
            self.db.query(query)
            return cliente.getInfo()
        except:
            return self.db.query(query)
    
    def login(self, login: Login):
        # caso o login nao seja concluido usar a linha abaixo
        # raise HTTPException(status_code=401, detail="Unauthorized")
        #busca um item na tabela cliente pelo id
        try :
            query = f"SELECT * FROM cliente WHERE email = '{login.email}' AND senha = '{login.password}' LIMIT 1;" 
            return Cliente.model_validate(self.db.query(query)[0]).getInfo()
        except:
            raise HTTPException(status_code=401, detail="Unauthorized")
    
    