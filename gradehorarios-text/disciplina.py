from aluno import Aluno
from professor import Professor
from sala import Sala
from semestre import Semestre

class Disciplina:
    
    def __init__(self, 
                 cod : str, 
                 semestre : int, 
                 nome : str, 
                 carga_horaria : int, 
                 e_tecnica : bool, 
                 sala : Sala):
        
        self.cod = cod
        self.semestre = semestre
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.e_tecnica = e_tecnica    
        self.sala = sala        
        self.horarios = list()        
        self.pre_requisitos = list()
        self.professor = None 
        self.alunos = list()
        
    def addHorario(self, horarios : list):
        self.horarios = horarios
        print(f"Horários adicionados à disciplina {self.nome}")

    def addAluno(self, aluno : Aluno):
        self.alunos.append(aluno)

    def addProfessor(self, professor : Professor):
        self.professor = professor

    def __repr__(self):
        # Isso aqui vai ser chamado quando tu fizer "print(nome_da_disciplina)"
        desc = f"""Disciplina: {self.nome} \n
        Professor: {self.professor.nome} \n
        Carga Horária: {self.carga_horaria}h \n
        Horários: {self.horarios}"""

        return desc