from Disciplina import Disciplina
from Professor import Professor
from Sala import Sala
from Turma import Turma
from Horario import Horario
from Aula import Aula

# Salas

sala1      = Sala(5, 30, False),
sala2      = Sala(6, 30, False),
sala3      = Sala(7, 30, False),
sala_lab1  = Sala(3, 30, True),
sala_lab2  = Sala(4, 30, True),
sala_lab3  = Sala(5, 30, True),

salas = [
    Sala(5, 30, False),
    Sala(6, 30, False),
    Sala(7, 30, False),
    Sala(3, 30, True),
    Sala(4, 30, True),
    Sala(5, 30, True),
]


    
  
# Professor com dois slots bloqueados
prof1 = Professor(1058981, "Thomaz Maia")
prof1.setHorarios_Bloqueados(("SEG", "M", "AB"))
prof1.setHorarios_Bloqueados(("SEG", "M", "CD"))

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
turma5 = Turma("S4", "M")

# Disciplinas
mat1 = Disciplina("mat1", 1, "matemática 1", 40, False)
pest = Disciplina("pest", 3, "programação estruturada", 80, True)
fis1 = Disciplina("fis1", 1, "física 1", 40, False)
port1 = Disciplina("port1", 1, "português 1", 40, False)
hist1 = Disciplina("hist1", 1, "história 1", 40, False)
engen = Disciplina("engen", 3, "engenharia de software", 80, True)
poo = Disciplina("poo", 3, "programação orientada a objetos", 80, True)
mat4 = Disciplina("mat4", 4, "matemática 4", 80, False)
ingl2 = Disciplina("ingl2", 2, "inglês 2", 40, False)
hist4 = Disciplina("hist4", 4, "história 4", 80, False)

# Alocacoes: (Disciplina, Turma)
alocacoes = [
    (mat1, turma1),
    (pest, turma2),
    (fis1, turma1),
]

# Gera individuo aleatorio
grade = Horario(prof2, alocacoes, salas)
grade.gerar_individuo_aleatorio()

# Imprime a grade em formato de tabela
print(grade)

# Inspeciona um slot diretamente
grade.horario_grade("SEG", "M", "AB")  

# print("Verificando SEG-M-AB (bloqueado, deve ser None):")
# print(" ", grade.grade["SEG"]["M"]["AB"])

# print("\nVerificando metodo vazio() em SEG-M-AB:")
# aula = grade.grade["QUA"]["M"]["AB"]
# if aula is None:
#     print("  Slot vazio (None)")
# else:
#     print("  vazio():", aula.vazio())
