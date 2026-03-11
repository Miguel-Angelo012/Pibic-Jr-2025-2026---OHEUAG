from aluno import addDisciplina

class Disciplina:
    
    def __init__(self, cod : str, semestre : str, nome : str, carga_horaria : int, pre_requisitos : list, professor : Professor, alunos : list, horarios : list, e_tecnica : bool, sala : Sala):
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