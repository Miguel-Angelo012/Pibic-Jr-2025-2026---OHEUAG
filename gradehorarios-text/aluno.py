from semestre import Semestre

class Aluno:

    def __init__(self,
                 matricula = int,
                 nome = str,
                 ):

        self.matricula = matricula
        self.nome = nome
        self.id_semestre = Semestre.getSemestreLetivo()
