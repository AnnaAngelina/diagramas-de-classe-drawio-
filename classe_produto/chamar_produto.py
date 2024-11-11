from co_produto import Produto

produtos_disp = []

def adicionar_produto():
    global produtos_disp
    novo_produto = Produto
    novo_produto.nome = input('Digite o nome do produto: ')
    novo_produto.codigo = int(input('Digite o código do produto: '))
    novo_produto.preco = float(input('Digite o preço do produto: '))
    novo_produto.estoque = int(input('Digite o estoque do produto: '))
    novo_produto.descricao = input('Descrição: ')
    produtos_disp.append(novo_produto)
    print('Produto adicionado com sucesso!\n')
def alterar_produtos():
    global produtos_disp
    quant = 0
    sem_esp = []
    for p in produtos_disp:
        if p.nome == '':
            quant+=1
            sem_esp.append(p)
    if quant == 0:
        print('Não há nenhum produto cadastrado sem especificações')
    else:
        print(f'Há {quant} produto(s) cadastrado(s) sem as especificações necessárias')
        esc = int(input('Deseja alterar algum? '))
        if esc in ('s', 'sim'):
            sem_esp[0].nome = input('Digite o novo nome do produto: ')
            sem_esp[0].codigo = int(input('Digite o novo código do produto: '))
            sem_esp[0].preco = float(input('Digite o novo preço do produto: '))
            sem_esp[0].estoque = int(input('Digite o novo estoque do produto: '))
            sem_esp[0].descricao = input('Descrição: ')
            print('Produto alterado com sucesso!\n')
def procurar(nome, codigo):
    global produtos_disp
    quant = 0
    for i in produtos_disp:
        if i.nome.lower() == nome.lower() and i.codigo == codigo:
            if quant == 0:
                print('Produtos encontrados: ')
                quant+=1
            i.exibir_Detalhes()
    if quant != 0:
        print('Esse produto não foi encontrado!')
def comprar(nome_produtos, preco, dinheiro):
    global produtos_disp
    val = True
    nome_produtos = input('Digite o nome do produto: ')
    for n in produtos_disp:
        if n.nome.lower() == nome_produtos.lower() and val:
            val = False
        if val == False:
            if preco > 10.0:
                print(f'Parabéns, você ganhou um desconto de {n.calcularDesconto(0.1)}')
                adc = input('Deseja adicionar a sua compra? ')
                if adc in ('s', 'sim'):
                    n.preco -= n.calcularDesconto(0.1)
            dinheiro-=n.preco
            if dinheiro != 0:
                print(f'O troco foi de R${dinheiro}')
            else:
                print('Obrigada pela compra!')

p1 = Produto()
produtos_disp.append(p1)
adicionar_produto()
alterar_produtos()
procurar('Cream Craker', 1120)
comprar('Caixa de chocolate', 11, 12)
