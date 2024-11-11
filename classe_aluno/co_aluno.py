class Aluno:
    '''A classe representa um aluno e suas características de estudante, tanto seus dados estudantis como suas utilidades dentro de um curso específico como se matricular em uma disciplina do curso, cancelar matrícula em uma disciplina e verificar sua nota'''
    def __init__(self, nome, matricula, curso, idade, email):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.idade = idade
        self.email = email
    def matricularEmDisciplina(self, disciplina):
        print(f'{self.nome.title()} foi matriculado(a) na disciplina de {disciplina}')
    def cancelarMatricula(self, disciplina):
        print(f'A matrícula de {self.nome.title()} foi cancelada na disciplina de {disciplina}')
    def consultarNota():
        return 9.8