from aula import Aula
from professor import Professor
from aluno import Aluno
from disciplina import Disciplina
from sala import Sala
from semestre import Semestre
from turma import Turma
import random

DIAS = ["SEG", "TER", "QUA", "QUI", "SEX"]
TURNOS = {
    "M" : ["AB", "CD"],
    "T" : ["AB", "CD"],
    "N" : ["AB", "CD"],
}
class Horario:
# horario.grade["SEG"]["M"]["AB"] -> retorna um objeto do tipo Aula
# horario.grade["SEG"]["M"]["AB"].turma -> retorna um objeto Turma
# horario.grade["SEG"]["M"]["AB"].vazio() -> retorna True se o slot tiver livre    

    def __init__(self, 
                professor: Professor, 
                alocacoes: list[tuple[Disciplina, Turma]],
                salas: list[Sala]
                ):
        
        self.professor = professor
        self.alocacoes = alocacoes
        self.salas = salas

        self.grade = self.inicializar_grade()
        
    def inicializar_grade(self):
        grade = {}

        for dia in DIAS:
            grade[dia] = {}

            for turno in TURNOS:
                grade[dia][turno] = {}

                for slot in TURNOS[turno]:
                    grade[dia][turno][slot] = None #Aula(Disciplina, Turma, Sala)

        return grade
    
    def gerar_individuo(self):
        # cria lista de aulas
        aulas = [
            Aula(alocacao=aloc, sala=random.choice(self.salas))
            for aloc in self.alocacoes
        ]

        # embaralha
        random.shuffle(aulas)

        i = 0
        for dia in DIAS:
            for turno in TURNOS:
                for slot in TURNOS[turno]:
                    
                    if i < len(aulas):
                        self.grade[dia][turno][slot] = aulas[i]
                        i += 1
                    else:
                        self.grade[dia][turno][slot] = Aula()  # vazio

sala = Sala(5, 30, False)
sala_lab = Sala(3, 30, True)

# Professor
prof1 = Professor(1058981, "Thomaz Maia")
prof1.setHorarios_Bloqueados(("SEG", "M", "AB"))
prof1.setHorarios_Bloqueados(("SEG", "M", "CD"))

# Turmas
turma1 = Turma("S1A", "D")
turma2 = Turma("S3", "D")

# Disciplinas
mat1 = Disciplina("mat1", 1, "matemática 1", 40, False)
pest = Disciplina("pest", 3, "programação estruturada", 80, True)
fis1 = Disciplina("fis1", 1, "física 1", 40, False)

aula1 = Aula((mat1, turma1), sala)

aula2 = Aula((pest, turma2), sala_lab)

alocacoes = [
    (mat1, turma1),
    (pest, turma2),
    (fis1, turma1)
]

grade = Horario(prof1, alocacoes, [sala, sala_lab])
grade.gerar_individuo()
print(sala)
print(aula1)
print(grade.grade)
