from abc import ABC, abstractmethod

# Classe abstrata representando os usuários do sistema
class Carro(ABC):
    def __init__(self, nome, modelo, descricao, img, id):
        self.id = id # se o usuário está logado
        self.modelo = modelo # id salvo no banco de dados remoto
        self.descricao = descricao # id unico
        self.nome = nome  # nome
        self.img = img  # nome
