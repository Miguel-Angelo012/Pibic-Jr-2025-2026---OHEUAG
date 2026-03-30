from aula import Aula
from disciplina import Disciplina
from professor import Professor
from sala import Sala
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
