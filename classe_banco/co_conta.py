class Conta():
    def __init__(self, numero, agencia, dono):
        self.numero = numero
        self.agencia = agencia
        self.dono = dono
        self.saldo = 0
    def depositar(self, valor):
        self.saldo += valor
        print(f'Foi depositado R${valor} em sua conta')
    def fazer_transferencia(self, destinatario, valor):
        destinatario.saldo = destinatario.saldo + valor
        self.saldo -= valor
        print('Transferência concluída!')