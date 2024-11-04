class Pessoinha():
    def __init__(self, nome, sobrenome, nascimento, sexo, nacionalidade, etnia):
        self.nomeesobrenoome = nome + sobrenome
        self.idade = 2024-int(nascimento)
        self.sexo = sexo
        self.nacionalidade = nacionalidade
        self.etnia = etnia
        self.comer = False
        self.beber = False
        self.dormir = False
        self.trabalhar = False
    def comer(self):
        if self.comer:
            print(self.nomeesobrenoome.title(), 'já está comendo')
        else:
            print(self.nomeesobrenoome.title(), 'começou a comer')
            self.comer = True
    def parar_comer(self):
        if self.comer:
            print(self.nomeesobrenoome.title(), 'parou de comer')
        else:
            print(self.nomeesobrenoome.title(), 'não está comendo')

    def beber(self):
        if self.beber:
            print(self.nomeesobrenoome.title(), 'já está bebendo')
        else:
            print(self.nomeesobrenoome.title(), 'começou a beber')
            self.beber = True
    def parar_beber(self):
        if self.beber:
            print(self.nomeesobrenoome.title(), 'parou de beber')
        else:
            print(self.nomeesobrenoome.title(), 'não está bebendo')

    def dormir(self):
        if self.dormir:
            print(self.nomeesobrenoome.title(), 'já está dormindo')
        else:
            print(self.nomeesobrenoome.title(), 'foi dormir')
            self.dormir = True
    def parar_dormir(self):
        if self.dormir:
            print(self.nomeesobrenoome.title(), 'acordou')
        else:
            print(self.nomeesobrenoome.title(), 'não está dormindo')

    def trabalhar(self):
        if self.trabalhar:
            print(self.nomeesobrenoome.title(), 'já está trabalhando')
        else:
            print(self.nomeesobrenoome.title(), 'foi trabalhar')
            self.trabalhar = True
    def parar_trabalhar(self):
        if self.trabalhar:
            print(self.nomeesobrenoome.title(), 'parou de trabalhar')
        else:
            print(self.nomeesobrenoome.title(), 'não está trabalhando')
    