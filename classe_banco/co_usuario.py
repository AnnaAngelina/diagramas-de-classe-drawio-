class Usuario():
    def __init__(self, nome, cpf, nascimento):
        self.nome = nome
        self.__cpf = cpf
        self.nascimento = nascimento