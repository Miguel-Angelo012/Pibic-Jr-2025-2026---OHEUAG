from Aula import Aula
from Disciplina import Disciplina
from Professor import Professor
from Sala import Sala
from Turma import Turma
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
                alocacoes: list,
                salas: list
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
                    grade[dia][turno][slot] = None

        return grade
    
    def gerar_individuo_aleatorio(self):
        todas_alocacoes = self.alocacoes.copy()
        random.shuffle(todas_alocacoes)

        # Monta lista apenas com slots NAO bloqueados pelo professor
        bloqueados = self.professor.getHorarios_Bloqueados()
        slots_disponiveis = []

        for dia in DIAS:
            for turno in TURNOS:
                for slot in TURNOS[turno]:
                    if (dia, turno, slot) not in bloqueados:
                        slots_disponiveis.append((dia, turno, slot))

        #  embaralha os slots
        random.shuffle(slots_disponiveis)

        # Aloca cada alocacao em um slot disponivel
        for i in range(len(todas_alocacoes)):


            if i >= len(slots_disponiveis):
                print(f"Aviso: slots do professor {self.professor} insuficientes para todas as alocacoes.")
                break
 
            alocacao = todas_alocacoes[i]
            dia, turno, slot = slots_disponiveis[i]
            disciplina = alocacao[0]

            # Verifica se a disciplina já possui um professor atribuido
            if disciplina.professor is not None: 
                print(f"A disciplina {disciplina}, já possui um professor")
                continue

            # Filtra salas compativeis com o tipo da disciplina (lab ou nao)
            salas_compativeis = []
            for sala in self.salas:
                
                # Verifica se a sala já está ocupada naquele horário
                if sala.esta_ocupada(dia, turno, slot):
                    print(f"Sala {sala} já está ocupada")
                    continue

                if sala.laboratorio == disciplina.e_tecnica:
                    salas_compativeis.append(sala)
 
            if len(salas_compativeis) == 0:
                print(f"Aviso: nenhuma sala compativel para {disciplina.nome}.")
                continue

            sala = random.choice(salas_compativeis)
            self.grade[dia][turno][slot] = Aula(alocacao, sala)
            disciplina.addProfessor(self.professor) # Atribuiu o professor a disciplina
            sala.ocupar(dia, turno, slot) # Ocupa aquela sala naquele horário
    
    def horario_grade(self, dia, turno, slot):  # retorna um objeto do tipo Aula
        
        aula = self.grade[dia][turno][slot]
        if aula is None:
            print("Slot vazio")
        else:
            if aula.sala.laboratorio == True:
                print(f"Matéria: {aula.disciplina.nome}\nTurma: {aula.turma.cod}\nLaboratório: {aula.sala.num_sala}")
            else:
                print(f"Matéria: {aula.disciplina.nome}\nTurma: {aula.turma.cod}\nSala: {aula.sala.num_sala}")
    
    def __repr__(self):
        # Cabecalho
        resultado = "\nGrade — Prof. " + self.professor.nome + "\n"
        resultado = resultado + f"{'':>8}"
        for dia in DIAS:
            resultado = resultado + f"{dia:^22}"
        resultado = resultado + "\n"
 
        # Linhas por turno e slot
        for turno in TURNOS:
            for slot in TURNOS[turno]:
                rotulo = turno + "-" + slot
                resultado = resultado + f"{rotulo:>8}"
 
                for dia in DIAS:
                    aula = self.grade[dia][turno][slot]
                    if aula is None:
                        celula = "—"
                    else:
                        celula = aula.disciplina.cod + "/" + aula.turma.cod
                    resultado = resultado + f"{celula:^22}"
 
                resultado = resultado + "\n"
 
            resultado = resultado + "\n"
 
        return resultado
