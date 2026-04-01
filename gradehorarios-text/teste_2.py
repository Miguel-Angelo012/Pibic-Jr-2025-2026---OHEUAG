from Aluno import Aluno
from Disciplina import Disciplina
from Professor import Professor
from Sala import Sala
from Semestre import Semestre
from Turma import Turma
from Horario import Horario
from Aula import Aula

# No futuro: 
# horario.grade["SEG"]["M"]["AB"] -> retorna um objeto do tipo Aula
# horario.grade["SEG"]["M"]["AB"].turma -> retorna um objeto Turma
# horario.grade["SEG"]["M"]["AB"].vazio() -> retorna True se o slot tiver livre

# Salas
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

alocacoes = [
    (mat1, turma1),
    (pest, turma2),
    (fis1, turma1)
]

aula1 = Aula(alocacoes[0], sala)
# print(aula1)

aula2 = Aula(alocacoes[1], sala_lab)
# print(aula2)

#Horario
grade_horarios1 = Horario(prof1, alocacoes, [sala, sala_lab])
grade_horarios1.gerar_individuo_aleatorio()
print(grade_horarios1.grade)
#horario = horario

