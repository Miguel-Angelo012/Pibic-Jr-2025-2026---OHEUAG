from Disciplina import Disciplina
from Professor import Professor
from Sala import Sala
from Turma import Turma
from Horario import Horario
from Aula import Aula

# Salas

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
prof1.setHorarios_Bloqueados(("SEG", "T", "AB"))
prof1.setHorarios_Bloqueados(("SEG", "T", "CD"))

# Só pra textar se 1 professor em cada disciplina esta funcionando:
# prof1.setHorarios_Bloqueados(("SEG", "N", "AB"))
# # prof1.setHorarios_Bloqueados(("SEG", "N", "CD"))
# prof1.setHorarios_Bloqueados(("TER", "M", "AB"))
# prof1.setHorarios_Bloqueados(("TER", "M", "CD"))
# prof1.setHorarios_Bloqueados(("TER", "T", "AB"))
# prof1.setHorarios_Bloqueados(("TER", "T", "CD"))
# prof1.setHorarios_Bloqueados(("TER", "N", "AB"))
# prof1.setHorarios_Bloqueados(("TER", "N", "CD"))
# prof1.setHorarios_Bloqueados(("QUA", "M", "AB"))
# prof1.setHorarios_Bloqueados(("QUA", "M", "CD"))
# prof1.setHorarios_Bloqueados(("QUA", "T", "AB"))
# prof1.setHorarios_Bloqueados(("QUA", "T", "CD"))
# prof1.setHorarios_Bloqueados(("QUA", "N", "AB"))
# prof1.setHorarios_Bloqueados(("QUA", "N", "CD"))
# prof1.setHorarios_Bloqueados(("QUI", "M", "AB"))
# prof1.setHorarios_Bloqueados(("QUI", "M", "CD"))
# prof1.setHorarios_Bloqueados(("QUI", "T", "AB"))
# prof1.setHorarios_Bloqueados(("QUI", "T", "CD"))
# prof1.setHorarios_Bloqueados(("QUI", "N", "AB"))
# prof1.setHorarios_Bloqueados(("QUI", "N", "CD"))
# prof1.setHorarios_Bloqueados(("SEX", "M", "AB"))
# prof1.setHorarios_Bloqueados(("SEX", "M", "CD"))
# prof1.setHorarios_Bloqueados(("SEX", "T", "AB"))
# prof1.setHorarios_Bloqueados(("SEX", "T", "CD"))
# prof1.setHorarios_Bloqueados(("SEX", "N", "AB"))
# prof1.setHorarios_Bloqueados(("SEX", "N", "CD"))


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

# S1
mat1 = Disciplina("mat1", 1, "matemática 1", 40, False)
fis1 = Disciplina("fis1", 1, "física 1", 40, False)
port1 = Disciplina("port1", 1, "português 1", 40, False)
hist1 = Disciplina("hist1", 1, "história 1", 40, False)
ingl1 = Disciplina("ingl1", 1, "ingles", 40, False)

# S2
mat2 = Disciplina("mat2", 2, "matemática 2", 40, False)
fis2 = Disciplina("fis2", 2, "física 2", 40, False)
port2 = Disciplina("port2", 2, "português 2", 40, False)
hist2 = Disciplina("hist2", 2, "história 2", 40, False)
ingl2 = Disciplina("ingl2", 2, "inglês 2", 40, False)

# S3
pest = Disciplina("pest", 3, "programação estruturada", 80, True)
engen = Disciplina("engen", 3, "engenharia de software", 80, True)
poo = Disciplina("poo", 3, "programação orientada a objetos", 80, True)
mat3 = Disciplina("mat3", 3, "matemática 3", 40, False)
fis3 = Disciplina("fis3", 3, "física 3", 40, False)
port3 = Disciplina("port3", 3, "português 3", 40, False)
hist3 = Disciplina("hist3", 3, "história 3", 40, False)
ingl3 = Disciplina("ingl3", 3, "inglês 3", 40, False)

# S4
mat4 = Disciplina("mat4", 4, "matemática 4", 80, False)
fis4 = Disciplina("fis4", 4, "física 4", 40, False)
port4 = Disciplina("port4", 4, "português 4", 40, False)
ingl4 = Disciplina("ingl4", 4, "inglês 4", 40, False)
hist4 = Disciplina("hist4", 4, "história 4", 80, False)

# Alocacoes: (Disciplina, Turma)
alocacoes = [
    (mat1, turma1),
    (port1, turma3),
    (hist1, turma3),
    (fis1, turma1),
    (ingl1, turma3),

    (mat2, turma4),
    (fis2, turma4),
    (ingl2, turma4),
    (port2, turma4),
    (hist2, turma4),

    (pest, turma2),
    (engen, turma2),
    (poo, turma2),
    (mat3, turma2),
    (fis3, turma2),
    (ingl3, turma2),
    (port3, turma2),
    (hist3, turma2),

    (mat4, turma5),
    (hist4, turma5),
    (ingl4, turma5),
    (port4, turma5),
    (fis4, turma5)
]

# Gera individuo aleatorio
grade1 = Horario(prof1, alocacoes, salas)
grade1.gerar_individuo_aleatorio()

grade2 = Horario(prof2, alocacoes, salas)
grade2.gerar_individuo_aleatorio()

# grade3 = Horario(prof3, alocacoes, salas)
# grade3.gerar_individuo_aleatorio()


# Imprime a grade em formato de tabela
print(grade1)
print(grade2)
# print(grade3)


# Inspeciona um slot diretamente
grade1.horario_grade("SEG", "N", "AB")  
grade1.horario_grade("SEG", "N", "CD")


grade2.horario_grade("SEG", "N", "AB")
grade2.horario_grade("SEG", "N", "CD")
# grade1.horario_grade("TER", "M", "AB")  
# grade1.horario_grade("TER", "M", "CD")  
# grade1.horario_grade("TER", "T", "AB")  
# grade1.horario_grade("TER", "T", "CD")    
# grade1.horario_grade("TER", "N", "AB")  
# grade1.horario_grade("TER", "N", "CD")  
# grade1.horario_grade("QUA", "M", "AB")  
# grade1.horario_grade("QUA", "M", "CD")  
# grade1.horario_grade("QUA", "T", "AB")  
# grade1.horario_grade("QUA", "T", "CD")  


