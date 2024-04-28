from src.infra.Database import Database
# from src.data.entities.cliente import Cliente
# from src.data.entities.login import Login
from fastapi import HTTPException
from datetime import datetime
from src.data.entities.body import ContratoBody
from src.data.control.AtendimentoDAO import AtendimentoDAO
from src.data.control.PagamentoDAO import PagamentoDAO

class ContratoDAO:
    def __init__(self):
        self.db =  Database()
        self.atendimentoDAO = AtendimentoDAO()
        self.pagamentoDAO = PagamentoDAO()
    
    def create(self, contrato: ContratoBody):
        print(contrato.forma_pagamento)

        date = datetime.now()
        query = f"INSERT INTO contrato (data, status, cliente_id) VALUES ( '{date}', 0, {contrato.cliente.id} );"
        contrato_id = self.db.query(query)

        valor = 0
        try:
            for atentimento in contrato.atendimentos:
                self.atendimentoDAO.create(atentimento, contrato_id)
                valor += atentimento.servico.preco
        except:
            print('erro')

        #PAGAMENTO

        #verifica desconto
        desconto_valido = True if contrato.cliente.e_flamengo or contrato.cliente.assiste_one_piece or contrato.cliente.cidade.lower() == 'sousa' else False
        desconto = valor * 0.1 if desconto_valido else 0
        valor_total = valor - desconto
       
        self.pagamentoDAO.create(contrato.forma_pagamento, contrato.cliente.id, contrato_id, valor, desconto, valor_total)

        return True
        
    
    
    