from co_pessoa import Pessoinha

pessoa1 = Pessoinha('Anna Angelina', 'Brito', 2008, 'F', 'Brasileira', 'Branca')
print(pessoa1.__nacionalidade) #dá erro quando pois nacionalidade ficou privado
print(type(pessoa1.comer()))
print(pessoa1.comer())
print(pessoa1.parar_comer())

