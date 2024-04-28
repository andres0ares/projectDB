from src.infra.Database import Database
# from src.data.entities.cliente import Cliente
# from src.data.entities.login import Login
from fastapi import HTTPException
from datetime import datetime
from src.data.entities.body import Atendimento

class AtendimentoDAO:
    def __init__(self):
        self.db =  Database()
    
    def create(self, atendimento: Atendimento, contrato_id: int):
    
        query = f"INSERT INTO atendimento (data_agendada, placa, carro_id, servico_id, contrato_id) VALUES ( '{atendimento.agendamento}', '{atendimento.placa}', {atendimento.carro.id}, {atendimento.servico.id}, {contrato_id});"
        return self.db.query(query)

        
    
    