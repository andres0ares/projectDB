from src.infra.Database import Database
from src.data.entities.body import Aprove

class PagamentoDAO:
    def __init__(self):
        self.db =  Database()
    
    def getPagamentos(self):
        return [
            {
                "value": 1,
                "label": "Cartão de Crédito/Débito"
            },
            {
                "value": 2,
                "label": "Boleto"
            },
            {
                "value": 3,
                "label": "Pix"
            },
            {
                "value": 4,
                "label": "Berries"
            }
        ]
    
    def create(self, forma_pagamento: int, id_cliente: int, id_contrato: int, valor: float, desconto: float, valor_total: float):

        options = ["cartao", "boleto", "pix", "berries"]

        query = f"INSERT INTO Pagamento (contrato_id, contrato_cliente_id, valor, desconto, valor_total, forma_pagamento) VALUES ({id_contrato}, {id_cliente}, {valor}, {desconto}, {valor_total}, {forma_pagamento});"

        self.db.query(query)
        
        query2 = f" INSERT INTO {options[forma_pagamento-1]} (confirmado, Pagamento_contrato_id, Pagamento_contrato_cliente_id) VALUES (0, {id_contrato}, {id_cliente});"

        return self.db.query(query2)
    
    def updateAprove(self, body: Aprove):

        options = ["cartao", "boleto", "pix", "berries"]

        query = f"UPDATE {options[body.forma_pagamento-1]} SET confirmado = 1  WHERE Pagamento_contrato_id = {body.contrato_id};"
        
        return self.db.query(query)
        
    

        