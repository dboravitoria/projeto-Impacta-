class Curso:

    def __init__(self, nome, descricao):
        #Note que neste exemplo, todos os atributos são públicos
        self.nome = nome
        self.descricao = descricao
    
    def get nome(self):
        return self.nome

    def get descricao(self):
        return self.descricao