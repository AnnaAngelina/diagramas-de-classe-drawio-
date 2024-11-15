from co_aluno import Aluno

a1 = Aluno('Anna Angelina', 20231094010041, 'Informática', 16, 'annaangeh169@gmail.com')
a1.matricularEmDisciplina('Fundamentos de lógica e algoritimo')
a1.cancelarMatricula('Fundamentos de lógica e algoritimo')

a2 =  Aluno('Letícia', 20231094010064, 'Informática', 16, 'leticia.maria02@gmail.com')
a1.matricularEmDisciplina('Banco de dados')
print(a1.consultarNota())
