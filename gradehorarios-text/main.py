from disciplina import Disciplina
from aluno import Aluno
from professor import Professor
from sala import Sala
from semestre import Semestre

sala = Sala(10, 30, False)
prof = Professor(1058981, "Thomaz Maia")
prof.setHorarios_Bloqueados("SEG-M-CD")

print(prof.getHorarios_Bloqueados())


matematica1 = Disciplina("MAT1", 1, "Matemática 1", 40, False, sala)
matematica1.addHorario("SEG-M-AB")
matematica1.addProfessor(prof)
matematica1.addAluno("Miguel")
matematica1.addAluno("Valdemir")
matematica1.addAluno("Pedro")

print(matematica1)

Miguel = Aluno(20250001, "Miguel", Semestre(1, 2025))

print(Miguel.nome)
