from src.data.entities.carro import Carro
from src.infra.Database import Database
from src.data.entities.cliente import Cliente
from src.data.entities.login import Login
from fastapi import HTTPException
 
class ClienteDAO:
    def __init__(self):
        self.db =  Database()
    
    # a fazer
    def create(self, cliente: Cliente):
        cliente.print()
        return True
    
    # a fazer
    def login(self, login: Login):
        # caso o login nao seja concluido usar a linha abaixo
        # raise HTTPException(status_code=401, detail="Unauthorized")
        return {"nome": f"{login.email}"}
    