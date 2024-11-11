class Produto:
    '''A classe representa um produto, seja de supermercado, farmácia, do setor automotivo, industrial. Esse produto quando comprad terá sua utilidade específica de acordo com o objetivo de compra e a descrição da especificidade dele'''
    nome = ''
    codigo = 0
    preco = 0.0
    estoque = 0
    descricao = ''
    def calcularDesconto(self, percentual):
        desconto = percentual*self.preco
        return desconto
    def atualizarEstoque(self, quantidade):
        self.estoque +=quantidade
        print('Estoque atualizado para ', self.estoque)
    def exibir_Detalhes(self):
        print(f'Nome do produto: {self.nome}\nCódigo do produto: {self.codigo}\nPreço do produto: {self.preco}\nEstoque: {self.estoque}\nDescrição do produto: {self.descricao}')