from semestre import Semestre

class Aluno:

    def __init__(self,
                 matricula = int,
                 nome = str,
                 id_semestre = Semestre):

        self.matricula = matricula
        self.nome = nome
        self.id_semestre = id_semestre
        
    def getDisciplina(self):
        from disciplina import Disciplina
        

