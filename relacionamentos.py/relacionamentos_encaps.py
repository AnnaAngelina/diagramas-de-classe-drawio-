class Cliente():
    __nome = ''
    __endereco = ''
    __cpf = ''
    __idade = ''
    def mudaCPF(self, cpf):
        self.__cpf = cpf

c1 = Cliente()
c1.__nome = 'Anna'
c1.__endereco = 'Major Sales'
c1.__cpf = '119.347.294-34'
c1.__idade = 16
print(c1.__cpf)
c1.mudaCPF('166.920.814-16')
print(c1.__cpf)
#encapsulamento: proteger atributos de acessoas externos, os métodos serão públicos mas os atributos serão privados pois precisamos acessar.
# get e set
# pega a informação para acessar sem ser diretamente (sempre retorna algo), salva e enviar algo.