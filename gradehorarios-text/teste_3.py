from Disciplina import Disciplina
from Professor import Professor
from Sala import Sala
from Turma import Turma
from Horario import Horario
from Aula import Aula

# Salas
sala      = Sala(5, 30, False)
sala_lab  = Sala(3, 30, True)

# Professor com dois slots bloqueados
prof1 = Professor(1058981, "Thomaz Maia")
prof1.setHorarios_Bloqueados(("SEG", "M", "AB"))
prof1.setHorarios_Bloqueados(("SEG", "M", "CD"))

# Turmas
turma1 = Turma("S1A", "M")
turma2 = Turma("S3",  "N")

# Disciplinas
mat1 = Disciplina("mat1", 1, "matemática 1",           40, False)
pest = Disciplina("pest", 3, "programação estruturada", 80, True)
fis1 = Disciplina("fis1", 1, "física 1",               40, False)

# Alocacoes: (Disciplina, Turma)
alocacoes = [
    (mat1, turma1),
    (pest, turma2),
    (fis1, turma1),
]

# Gera individuo aleatorio
grade = Horario(prof1, alocacoes, [sala, sala_lab])
grade.gerar_individuo_aleatorio()

# Imprime a grade em formato de tabela
print(grade)

# Inspeciona um slot diretamente
print("Verificando SEG-M-AB (bloqueado, deve ser None):")
print(" ", grade.grade["SEG"]["M"]["AB"])

print("\nVerificando metodo vazio() em SEG-M-AB:")
aula = grade.grade["SEG"]["M"]["AB"]
if aula is None:
    print("  Slot vazio (None)")
else:
    print("  vazio():", aula.vazio())