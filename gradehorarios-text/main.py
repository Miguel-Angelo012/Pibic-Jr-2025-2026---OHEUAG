from disciplina import Disciplina
from aluno import Aluno
from professor import Professor
from sala import Sala
from semestre import Semestre

sala = Sala(10, 30, False)
prof = Professor(1058981, "Thomaz Maia")

matematica1 = Disciplina("MAT1", 1, "Matemática 1", 40, False, sala)
matematica1.addHorario(["SEG-M-AB", "QUA-M-CD"])
matematica1.addProfessor(prof)

print(matematica1)