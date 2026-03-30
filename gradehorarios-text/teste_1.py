from disciplina import Disciplina
from aluno import Aluno
from professor import Professor
from sala import Sala
from semestre import Semestre

prof1 = Professor(1058981, "Thomaz Maia")
prof1.setHorarios_Bloqueados( ("SEG", "M", "CD") )

prof2 = Professor(1058982, "Maria Silva")
prof2.setHorarios_Bloqueados( ("SEG", "M", "AB") )

print(prof1.getHorarios_Bloqueados())

matematica1 = Disciplina("MAT1", 1, "Matemática 1", 40, False)
matematica1.addHorario( ("SEG", "M", "AB") )

matematica1.addProfessor(prof2) # Não pode deixar
matematica1.addProfessor(prof1) # Ok

sala = Sala(10, 30, False)
matematica1.addSala(sala)

semestre_atual = Semestre(1, 2026)
aluno1 = Aluno(123, "Miguel", semestre_atual)
aluno2 = Aluno(124, "Valdemir", semestre_atual)
aluno3 = Aluno(125, "Pedro", semestre_atual)

matematica1.addAluno(aluno1)
matematica1.addAluno(aluno2)
matematica1.addAluno(aluno3)

print(matematica1)
