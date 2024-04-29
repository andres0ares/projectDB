from src.data.entities.funcionario import Funcionario
from src.infra.Database import Database
from src.data.entities.login import Login
from fastapi import HTTPException
 
class FuncionarioDAO:
    def __init__(self):
        self.db =  Database()

    def getAll(self):
       #retorna todos os itens da tabela carro
        query = "SELECT * FROM funcionario;"
        return [Funcionario.model_validate(funcionario) for funcionario in self.db.query(query)]
    
    def create(self, funcionario: Funcionario):
        #cria um novo item da tabela carro
        query = f"INSERT INTO funcionario (nome, email, senha ) VALUES ('{funcionario.nome}', '{funcionario.email}', '{funcionario.senha}');"

        return self.db.query(query)
    
    def login(self, login: Login):
        # caso o login nao seja concluido usar a linha abaixo
        # raise HTTPException(status_code=401, detail="Unauthorized")
        #busca um item na tabela cliente pelo id
        try :
            query = f"SELECT * FROM funcionario WHERE email = '{login.email}' AND senha = '{login.password}' LIMIT 1;" 
            return Funcionario.model_validate(self.db.query(query)[0]).getInfo()
        except:
            raise HTTPException(status_code=401, detail="Unauthorized")
    
    def update(self, funcionario: Funcionario):
        funcionario.print()
        return True
    