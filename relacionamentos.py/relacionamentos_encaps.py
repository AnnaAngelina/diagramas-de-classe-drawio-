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
print(c1.__cpf)
c1.mudaCPF('166.920.814-16')
print(c1.__cpf)
#encapsulamento: proteger atributos de acessoas externos, os métodos serão públicos mas os atributos serão privados pois precisamos acessar.
# get e set(usados no encapsulamento para manusear atributos privados uma vez que eles não devem ser acessados diretamente por segurança)
# o get pega a informação para acessar, sempre retorna algo, ou seja, lê e armazena o dado do objeto. Enquanto o set altera ou atribui valores a membros de dados.