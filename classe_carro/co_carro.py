class Carro:
    '''A classe representa um carro, com suas características tais como sua marca, modelo, ano, cor e preço a serem registrados. Um carro é usado para se deslocar com mais facilidade e praticidade de um lugar para outro utilidade de um carro pode variar, ele pode ser comprado a fins de viagens, trabalho, objeto para colecionadores'''
    def __init__(self, marca, modelo, ano, cor, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.preco = preco
    def acelerar(self):
        print('O carro acelerou!')
    def frear(self):
        print('O carro freou!')
    def ligar(self):
        print('O carro ligou')
