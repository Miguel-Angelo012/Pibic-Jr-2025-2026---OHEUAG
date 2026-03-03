class aluno:

    def __init__(self, matricula, historico):
        self.matricula = matricula
        self.historico = historico

    def participarAula():
        print(f"O {aluno} participou da aula")

    def solicitarComprovanteMatricula():
        print(f"O {aluno} solicitou um comprovante de matrícula")

    def solicitarNota():
        pass



class disciplina:

    def __init__(self, cod, nome, carga_horaria, pre_requisitos):
        self.cod = cod
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.pre_requisitos = pre_requisitos

    def verificarPreRequisitos():
        pass

class professor:

    def __init__(self, matricula, nome, horarios_livres, dias_livres):
        self.matricula = matricula
        self.nome = nome
        self.horarios_livres = horarios_livres
        self.dias_livres = dias_livres

    def ministrarAula():
        print(f"O professor {nome} deu aula de  para o semestre 1  ")