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
                 e_tecnica : bool):
        
        #Definidos por parâmetros
        self.cod = cod
        self.semestre = semestre
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.e_tecnica = e_tecnica    

        #Definidos por função
        self.horarios = list()        
        self.pre_requisitos = list()
        self.professor = None
        self.alunos = list()
        self.sala = None
        
    def addHorario(self, horarios : list):
        self.horarios.append(horarios)
        print(f"Horários adicionados à disciplina {self.nome}")


    def addAluno(self, aluno : Aluno):
        self.alunos.append(aluno)


    def addProfessor(self, professor : Professor):
        
        #Prevenção caso o professor tenha um horário bloqueado que coincida com o horário da disciplina
        for item in professor.getHorarios_Bloqueados():
            if item in self.horarios:
                print("O professor não pode ser adicionado neste horário!")
                return

        #Prevençao caso a disciplina já tenha um professor atribuído
        if self.professor is not None:
            print("A disciplina já tem um professor atribuído!")
            return

        self.professor = professor.nome


    def addSala(self, sala : Sala):

        if sala.laboratorio != self.e_tecnica:
            print(f"Esta sala não é adequada para {self.nome}")
            return

        self.sala = sala.num_sala


    def __repr__(self):
        #Caso a disciplina não tenha um professor atribuído.
        if self.professor is None:
            self.professor = "Sem professor"
        
        if not self.alunos:
            self.alunos = "Sem alunos"

        if not self.horarios:
            self.horarios = "Sem horários"

        if self.sala is None:
            self.sala = "Sem sala"

        # Isso aqui vai ser chamado quando tu fizer "print(nome_da_disciplina)"
        desc = f"""Disciplina: {self.nome} \n
        Professor: {self.professor} \n
        Carga Horária: {self.carga_horaria}h \n
        Horários: {self.horarios} \n
        Sala: {self.sala} \n
        Alunos: {self.alunos} \n
        """
        
        return desc
