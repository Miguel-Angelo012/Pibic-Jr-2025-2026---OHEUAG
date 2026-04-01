from Aula import Aula
from Professor import Professor
from Aluno import Aluno
from Disciplina import Disciplina
from Sala import Sala
from Semestre import Semestre
from Turma import Turma
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
    
    def gerar_individuo_aleatorio(self):
        todas_alocacoes = self.alocacoes.copy()
        random.shuffle(todas_alocacoes)

        todos_slots = []

        for dia in DIAS:
            for turno in TURNOS:
                for slot in TURNOS[turno]:
                    todos_slots.append((dia, turno, slot))

        #  embaralha os slots
        random.shuffle(todos_slots)

        for alocacao, (dia, turno, slot) in zip(todas_alocacoes, todos_slots):
            sala = random.choice(self.salas)
            self.grade[dia][turno][slot] = Aula(alocacao, sala)

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
grade.gerar_individuo_aleatorio()
print(grade.grade)

