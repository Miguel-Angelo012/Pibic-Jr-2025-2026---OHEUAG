from disciplina import Disciplina
from aluno import Aluno
from professor import Professor
from sala import Sala
from semestre import Semestre

sala = Sala(10, 30, True)

prof = Professor(1058981, "Thomaz Maia")
prof.setHorarios_Bloqueados("SEG-M-CD")

prof2 = Professor(1058982, "Maria Silva")
prof2.setHorarios_Bloqueados("SEG-M-AB")
print(prof.getHorarios_Bloqueados())


matematica1 = Disciplina("MAT1", 1, "Matemática 1", 40, False)
matematica1.addHorario("SEG-M-AB")
matematica1.addProfessor(prof2)
matematica1.addProfessor(prof)
matematica1.addSala(sala)
matematica1.addAluno("Miguel")
matematica1.addAluno("Valdemir")
matematica1.addAluno("Pedro")

print(matematica1)
