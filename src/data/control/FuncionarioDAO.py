from src.data.entities.funcionario import Funcionario
from src.infra.Database import Database
from src.data.entities.login import Login
from fastapi import HTTPException
 
class FuncionarioDAO:
    def __init__(self):
        self.db =  Database()

    # a fazer
    def getAll(self):
        staffs = [
            {
                'id': 1,
                'nome': 'Fulano',
                'email': 'fulano@gmail.com',
                'senha': 'fulano123',
            },
            {
                'id': 2,
                'nome': 'Fulano de Tal',
                'email': 'fulano2@gmail.com',
                'senha': 'fulano123',
            }
        ]

        return staffs
    
    # a fazer
    def create(self, funcionario: Funcionario):
        funcionario.print()
        return True
    
    # a fazer
    def login(self, login: Login):
        # caso o login nao seja concluido usar a linha abaixo
        # raise HTTPException(status_code=401, detail="Unauthorized")
        return {"nome": f"{login.email}"}
    
    def update(self, funcionario: Funcionario):
        funcionario.print()
        return True
    