from co_carro import Carro

carros_disp = []
carro1 = Carro('Chevrolet', 'Onix', 2023, 'Prata', 'R$80000')
carro2 = Carro('Hyundai', 'Creta', 2020, 'Cinza', 'R$75000')
carros_disp.append(carro1)
carros_disp.append(carro2)

def adicionar_carro():
    marca = input('Digite a marca do carro: ')
    modelo = input('Digite o modelo do carro: ')
    ano = int(input('Digite o ano do carro: '))
    cor = input('Digite a cor do carro: ')
    preco = input('Digite o preço do carro: ')
    novo_carro = Carro(marca, modelo, ano, cor, preco)
    carros_disp.append(novo_carro)
def procurar(marca, modelo, ano, cor, preco):
    quant = 0
    for i in carros_disp:
        if i.marca == marca and i.modelo == modelo and i.ano == ano and i.cor == cor and i.preco == preco:
            quant+=1
    if quant == 0:
        print('Não há carros com essas especificaçõe disponíveis!')
    else:
        print(f'Há {quant} carro(s) com essas especificações disponíveis!')
def testar_carro(marca, modelo, ano, cor, preco):
    lim = 0
    for c in carros_disp:
        if c.marca == marca and c.modelo == modelo and c.ano == ano and c.cor == cor and c.preco == preco and lim == 0:
            lim+=1
            c.ligar()
            funcao = input('Olá vamos testar os carro(s) com essas especificações. Você deseja acelerar ou frear? ')
            if funcao.lower() == 'acelerar':
                c.acelerar()
            else:
                c.frear()
    if lim == 0:
        print('Não foi encontrado carro(s) com essas especificações!')

adicionar_carro()
procurar('Chevrolet', 'Onix', 2023, 'Prata', 'R$80000')
testar_carro('Hyundai', 'Creta', 2020, 'Cinza', 'R$75000')
        