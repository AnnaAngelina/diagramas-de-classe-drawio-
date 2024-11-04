class Pessoinha():
    def __init__(self, nome, sobrenome, nascimento, sexo, nacionalidade, etnia):
        self.nome = nome + ' '+ sobrenome
        self.idade = 2024-int(nascimento)
        self.sexo = sexo
        self.nacionalidade = nacionalidade
        self.etnia = etnia
        self.come = False
        self.bebe = False
        self.dorme = False
        self.trabalha = False
    def comer(self):
        if self.come:
            return str(self.nome.title()) + ' já está comendo'
        else:
            self.come = True
            return str(self.nome.title()) + ' começou a comer'
                   
    def parar_comer(self):
        if self.come:
            self.come = False
            return str(self.nome.title())+ ' parou de comer'
        else:
            return str(self.nome.title())+ ' não está comendo'

    def beber(self):
        if self.bebe:
            return str(self.nome.title())+ ' já está bebendo'
        else:
            self.bebe = True
            return str(self.nome.title())+ ' começou a beber'
            
    def parar_beber(self):
        if self.bebe:
            self.bebe = False
            return str(self.nome.title())+ ' parou de beber'
        else:
            return str(self.nome.title())+ ' não está bebendo'

    def dormir(self):
        if self.dorme:
            return str(self.nome.title())+ ' já está dormindo'
        else:
            self.dorme = True
            return str(self.nome.title())+ ' foi dormir'
            
    def parar_dormir(self):
        if self.dorme:
            self.dorme = False
            return str(self.nome.title())+ ' acordou'
        else:
            return str(self.nome.title())+ ' não está dormindo'

    def trabalhar(self):
        if self.trabalha:
            return str(self.nome.title())+ ' já está trabalhando'
        else:
            self.trabalha = True
            return str(self.nome.title())+ ' foi trabalhar'
            
    def parar_trabalhar(self):
        if self.trabalha:
            self.trabalha = False
            return str(self.nome.title())+ ' parou de trabalhar'
        else:
            return str(self.nome.title())+ ' não está trabalhando'