class Pessoa():
    def __init__(self, nome, idade, profissao, rg):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.rg = rg
        
    def andar(self):
        print(self.nome, 'está andando')
    def falar(self):
        return (f'{self.nome} está falando')
    def trabalhar(self):
        print(self.nome, 'está trabalhando')

pesso1 = Pessoa('Anna', 15, 'Programadora', 004.087-19)
print(type(pesso1.falar()))