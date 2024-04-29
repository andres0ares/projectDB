from src.infra.Database import Database
# from src.data.entities.cliente import Cliente
# from src.data.entities.login import Login
from fastapi import HTTPException
import datetime
from src.data.entities.body import Atendimento

class AtendimentoDAO:
    def __init__(self):
        self.db =  Database()
    
    def create(self, atendimento: Atendimento, contrato_id: int):
    
        query = f"INSERT INTO atendimento (data_agendada, placa, carro_id, servico_id, contrato_id) VALUES ( '{atendimento.agendamento}', '{atendimento.placa}', {atendimento.carro.id}, {atendimento.servico.id}, {contrato_id});"
        return self.db.query(query)

    def getAtendimentosFormat(self):
    
        qtd_funcionarios = self.db.query("SELECT COUNT(*) AS t FROM funcionario;")[0]['t']

        dias_disponiveis = self.db.query("CALL dias_disponiveis();")

        # Cria uma lista vazia para armazenar os dicionários
        lista = []

        # Obtém a data atual
        data_atual = datetime.date.today()

        # Para cada dia nos próximos 31 dias
        for i in range(32):
            # Calcula a nova data
            nova_data = data_atual + datetime.timedelta(days=i)
            
            # Verifica se o dia da semana é sábado (5) ou domingo (6)
            if nova_data.weekday() in [5, 6]:
                qtd = 0
            else:
                qtd = qtd_funcionarios
            
            # Cria um novo dicionário com a data e a quantidade
            dicionario = {'dia': nova_data, 'qtd': qtd}
            
            # Adiciona o dicionário à lista
            lista.append(dicionario)


        for item in dias_disponiveis:
            find = next((i for i in lista if i["dia"] == item['data_agendada']), None)
            # Se o item foi encontrado
            if find is not None:
                # Modifica a quantidade
                find["qtd"] -= item['quantidade_atendimentos'] # substitua nova_quantidade pelo valor desejado
        
        return lista
    