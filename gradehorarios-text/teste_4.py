from Disciplina import Disciplina
from Professor import Professor
from Sala import Sala
from Turma import Turma
from Horario import Horario

# Salas
salas = [
    Sala(5, 30, False),
    Sala(6, 30, False),
    Sala(7, 30, False),
    Sala(3, 30, True),
    Sala(4, 30, True),
    Sala(8, 30, True),
]

# Professores
prof1 = Professor(1058981, "Thomaz Maia")
prof1.setHorarios_Bloqueados(("SEG", "M", "AB"))
prof1.setHorarios_Bloqueados(("SEG", "M", "CD"))
prof1.setHorarios_Bloqueados(("SEG", "T", "AB"))
prof1.setHorarios_Bloqueados(("SEG", "T", "CD"))

prof2 = Professor(1058982, "Maria Silva")
prof2.setHorarios_Bloqueados(("TER", "N", "AB"))
prof2.setHorarios_Bloqueados(("QUA", "M", "CD"))
prof2.setHorarios_Bloqueados(("QUI", "T", "AB"))

prof3 = Professor(1058983, "Carlos Oliveira")
prof3.setHorarios_Bloqueados(("QUA", "N", "AB"))
prof3.setHorarios_Bloqueados(("QUI", "M", "CD"))

prof4 = Professor(1058984, "Ana Costa")
prof4.setHorarios_Bloqueados(("TER", "M", "AB"))
prof4.setHorarios_Bloqueados(("QUI", "N", "CD"))
prof4.setHorarios_Bloqueados(("SEX", "T", "AB"))
prof4.setHorarios_Bloqueados(("SEX", "N", "CD"))

prof5 = Professor(1058985, "Luiz Santos")
prof5.setHorarios_Bloqueados(("SEG", "N", "AB"))
prof5.setHorarios_Bloqueados(("TER", "T", "CD"))
prof5.setHorarios_Bloqueados(("QUA", "M", "AB"))

# Turmas
turma1 = Turma("S1A", "M")
turma2 = Turma("S3",  "N")
turma3 = Turma("S1B", "M")
turma4 = Turma("S2",  "N")
turma5 = Turma("S4",  "M")

# Disciplinas
mat1  = Disciplina("mat1",  1, "matematica 1",                   2, False)
fis1  = Disciplina("fis1",  1, "fisica 1",                       2, False)
port1 = Disciplina("port1", 1, "portugues 1",                    2, False)
hist1 = Disciplina("hist1", 1, "historia 1",                     2, False)
ingl1 = Disciplina("ingl1", 1, "ingles 1",                       2, False)
mat2  = Disciplina("mat2",  2, "matematica 2",                   2, False)
fis2  = Disciplina("fis2",  2, "fisica 2",                       2, False)
port2 = Disciplina("port2", 2, "portugues 2",                    2, False)
hist2 = Disciplina("hist2", 2, "historia 2",                     2, False)
ingl2 = Disciplina("ingl2", 2, "ingles 2",                       2, False)
pest  = Disciplina("pest",  3, "programacao estruturada",        2, True)
engen = Disciplina("engen", 3, "engenharia de software",         2, True)
poo   = Disciplina("poo",   3, "programacao orientada objetos",  2, True)
mat3  = Disciplina("mat3",  3, "matematica 3",                   2, False)
fis3  = Disciplina("fis3",  3, "fisica 3",                       2, False)
port3 = Disciplina("port3", 3, "portugues 3",                    2, False)
hist3 = Disciplina("hist3", 3, "historia 3",                     2, False)
ingl3 = Disciplina("ingl3", 3, "ingles 3",                       2, False)
mat4  = Disciplina("mat4",  4, "matematica 4",                   2, False)
fis4  = Disciplina("fis4",  4, "fisica 4",                       2, False)
port4 = Disciplina("port4", 4, "portugues 4",                    2, False)
hist4 = Disciplina("hist4", 4, "historia 4",                     2, False)
ingl4 = Disciplina("ingl4", 4, "ingles 4",                       2, False)

# -------------------------------------------------------------------
# CORRECAO (Problema 1): alocacoes separadas por professor.
# Antes, uma lista unica com todas as disciplinas era passada para
# todos os professores. Isso fazia com que o primeiro professor
# "ocupasse" as disciplinas e os demais recebessem o aviso
# "A disciplina X ja possui um professor".
# Agora cada professor recebe apenas as disciplinas que lhe cabem.
# -------------------------------------------------------------------

alocacoes_prof1 = [
    (mat1,  turma1),
    (mat2,  turma4),
    (mat3,  turma2),
    (mat4,  turma5),
]

alocacoes_prof2 = [
    (pest,  turma2),
    (engen, turma2),
    (poo,   turma2),
]

alocacoes_prof3 = [
    (fis1,  turma1),
    (fis2,  turma4),
    (fis3,  turma2),
    (fis4,  turma5),
]

alocacoes_prof4 = [
    (port1, turma3),
    (port2, turma4),
    (port3, turma2),
    (port4, turma5),
    (ingl1, turma3),
    (ingl2, turma4),
]

alocacoes_prof5 = [
    (hist1, turma3),
    (hist2, turma4),
    (hist3, turma2),
    (hist4, turma5),
    (ingl3, turma2),
    (ingl4, turma5),
]

# Gera e imprime as grades
grade1 = Horario(prof1, alocacoes_prof1, salas)
grade1.gerar_individuo_aleatorio()

grade2 = Horario(prof2, alocacoes_prof2, salas)
grade2.gerar_individuo_aleatorio()

grade3 = Horario(prof3, alocacoes_prof3, salas)
grade3.gerar_individuo_aleatorio()

grade4 = Horario(prof4, alocacoes_prof4, salas)
grade4.gerar_individuo_aleatorio()

grade5 = Horario(prof5, alocacoes_prof5, salas)
grade5.gerar_individuo_aleatorio()

print(grade1)
print(grade2)
print(grade3)
print(grade4)
print(grade5)

# -------------------------------------------------------------------
# Verifica se salas sao limpas corretamente entre individuos (Problema 4)
# Gerando uma segunda rodada com os mesmos objetos de sala —
# nao deve haver bloqueios residuais da primeira geracao.
# -------------------------------------------------------------------

print("=" * 60)
print("Segunda geracao (teste de limpeza de ocupacao das salas)")
print("=" * 60)

grade1b = Horario(prof1, alocacoes_prof1, salas)
grade1b.gerar_individuo_aleatorio()
print(grade1b)