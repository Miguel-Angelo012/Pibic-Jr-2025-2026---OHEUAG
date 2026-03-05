from aluno import addDisciplina

class Disciplina:
    
    def __init__(self, cod, semestre, nome, carga_horaria, pre_requisitos, professor, alunos, horarios, e_tecnica, sala):
        self.cod = cod
        self.semestre = semestre
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.pre_requisitos = pre_requisitos
        # self.professor = Professor 
        # self.alunos = Aluno 
        self.horarios = horarios
        self.e_tecnica = e_tecnica
        # self.sala = Sala 
        
        def addAluno(Aluno):
            pass

        def addProfessor(Professor):
            pass
    
        def addSala(Sala):
            pass