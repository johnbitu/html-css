class Pessoa:
    def __init__(self,nome,idade,falando=False,comendo=False):
        self.nome = nome
        self.idade = idade
        self.falando = falando
        self.comendo = comendo

    def comer(self):
        print(f'{self.nome} está comendo')