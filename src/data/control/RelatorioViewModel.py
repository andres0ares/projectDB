from src.data.control.CarroDAO import CarroDAO


class Relatorio:
    def __init__(self):
        pass

    def getList(self):
        return [
            { 
                "option": 0,
                "name": "Carros disponíveis",
                "subtitle": "Lista de todos os carros disponíveis."
            },
            { 
                "option": 1,
                "name": "Relótorio test 2",
                "subtitle": "Apenas para teste"
            }
        ]
    

    def get(self, option: int):

        options = {
            0: self.option0,
            1: self.option1
        }

        return options.get(option)()
    
    def option0(self):
        carHandle = CarroDAO()
        return carHandle.getCarros()
    
    def option1(self):
        return [
            {
                "item": "exemplo 1",
                "item 2": "exemplo 1",
                "item 3": "exemplo 1",
                "item 4": "exemplo 1",
            },
            {
                "item": "exemplo 2",
                "item 2": "exemplo 2",
                "item 3": "exemplo 2",
                "item 4": "exemplo 2",
            },
            {
                "item": "exemplo 3",
                "item 2": "exemplo 3",
                "item 3": "exemplo 3",
                "item 4": "exemplo 3",
            }
        ]
     
    
    