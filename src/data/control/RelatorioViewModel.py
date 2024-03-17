from src.data.control.CarroDAO import CarroDAO


class Relatorio:
    def __init__(self):
        pass

    def getList(self):
        # titulos dos relatorios exibidos no sistema
        return [
            { 
                "option": 0,
                "name": "Carros disponíveis",
                "subtitle": "Lista de todos os carros disponíveis."
            },
            { 
                "option": 1,
                "name": "Quantidades",
                "subtitle": "Quantidades de itens cadastrados no sistema."
            }
        ]
    

    def get(self, option: int):
        # retorna o handle do tipo de relatorio
        options = {
            0: self.option0,
            1: self.option1
        }

        return options.get(option)()
    
    def option0(self):
        #implementa o relatorio 1 a lista de carros cadastrados
        carHandle = CarroDAO()
        return carHandle.getAll()
    
    def option1(self):
        #implementa o relatorio 2 com as quantidades dos itens:
        carHandle = CarroDAO()
        return [
            {
                " ": "Quantidade de carros cadastrados:",
                "Quantidade": len(carHandle.getAll())
            },
            {
                " ": "Quantidade de clientes cadastrados:",
                "Quantidade": 0
            },
            {
                " ": "Quantidade de vendedores cadastrados:",
                "Quantidade": 0
            }
        ]
    
     
    
    