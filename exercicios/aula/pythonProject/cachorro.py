class Cachorro:
    def __init__(self):
        self.raca = 'Golden Retriever'
        self.nome = 'Bolt'

    def Raça(self):
        print(self.raca)

    def Nome(self):
        print(self.nome)

    def Latir(self):
        print('Au Au')

cachorro1 = Cachorro()
cachorro1.Raça()
cachorro1.Latir()
