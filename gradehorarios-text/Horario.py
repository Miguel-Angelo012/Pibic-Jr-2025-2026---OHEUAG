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
# Restrições rígidas que faltam:
# 7. O horário de cada professor deve começar com pelo menos 20h livres;


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

        self.horario_valido = True

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

        if not self.check_horas_livres_minimas():
            self.horario_valido = False
            return

        todas_alocacoes = self.alocacoes.copy()
        random.shuffle(todas_alocacoes)

        # Limpa a ocupacao das salas antes de gerar, evitando que slots ocupados num individuo anterior bloqueiem este.
        for sala in self.salas:
            sala.limpar_ocupacao()

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
        for alocacao in todas_alocacoes:

            disciplina = alocacao[0]
            alocado = False

            for dia, turno, slot in slots_disponiveis:

                # slot ocupado
                if self.grade[dia][turno][slot] is not None:
                    continue

                # professor bloqueado
                if (dia, turno, slot) in bloqueados:
                    continue

                # noite/manhã
                dia_atual = DIAS.index(dia)
                if self.check_noite_manha(dia_atual, turno, slot):
                    continue

                # limite de aulas
                if self.check_aulas_no_dia(dia) >= 6:
                    continue

                # dias concentrados
                if self.professor.getDias_concentrados():
                    if not self.check_dias_concentrados(dia):
                        continue

                salas_compativeis = self.check_salas(dia, turno, slot, disciplina)

                if len(salas_compativeis) == 0:
                    continue

                sala = random.choice(salas_compativeis)

                self.grade[dia][turno][slot] = Aula(alocacao, sala)
                sala.ocupar(dia, turno, slot)

                alocado = True
                break

            if not alocado:
                print(f"Nao foi possível alocar {disciplina.nome}")
    
    def funcao_fitness(self):
        
        pontuacao = 0
        
        # Restrições Rígidas:

        if not self.rr4_check_dias_livres():
            pontuacao += 10

        if not self.rr5_dias_concentrados():   
            pontuacao += 10

        if not self.rr7_horas_livres():
            pontuacao += 10

        if not self.rr8_salas_ocupadas():
            pontuacao += 10

        if not self.rr9_labs_tecnicos():
            pontuacao += 10

        if not self.rr10_limite_aulas():
            pontuacao += 10

        if not self.rr11_check_noite_manha():
            pontuacao += 10

        # Restrições Flexíveis:

        pontuacao += self.rf1_quatro_aulas_seguidas() * 5

        pontuacao += self.rf5_evitar_janelas() * 4

        pontuacao += self.rf2_mesma_turma_mesmo_professor() * 3

        pontuacao += self.rf3_priorizar_inicio_fim_livre() * 3

        pontuacao += self.rf6_concentrar_disciplinas() * 2

        pontuacao += self.rf4_priorizar_manha() * 1

        # resta apenas a rf7

        print(pontuacao)
    
    # Funções Booleanas para Fitness Funtion
    
    # Restrições Rígidas

    def rr4_check_dias_livres(self): # RR 4

        bloqueados = self.professor.getHorarios_Bloqueados()

        for dia, turno, slot in bloqueados:

            if self.grade[dia][turno][slot] is not None:
                return False

        return True
    
    def rr5_dias_concentrados(self): # RR 5

        if not self.professor.getDias_concentrados():
            return True

        dias_utilizados = self.get_indices_dias_utilizados()

        for i in range(len(dias_utilizados) - 1):

            if dias_utilizados[i + 1] - dias_utilizados[i] > 1:
                return False

        return True
    
    def rr6_check_turnos_bloqueados(self): # RR 6

        bloqueados = self.professor.getHorarios_Bloqueados()

        for dia, turno, slot in bloqueados:

            if self.grade[dia][turno][slot] is not None:
                return False

        return True
    
    def rr7_horas_livres(self): # RR 7
        return self.check_horas_livres_minimas()
    
    def rr8_salas_ocupadas(self): # RR 8

        ocupacoes = set()

        for dia in DIAS:
            for turno in TURNOS:
                for slot in TURNOS[turno]:

                    aula = self.grade[dia][turno][slot]

                    if aula is None:
                        continue

                    chave = (aula.sala.num_sala, dia, turno, slot)

                    if chave in ocupacoes:
                        return False

                    ocupacoes.add(chave)

        return True

    def rr9_labs_tecnicos(self): # RR 9

        for dia in DIAS:
            for turno in TURNOS:
                for slot in TURNOS[turno]:

                    aula = self.grade[dia][turno][slot]

                    if aula is None:
                        continue

                    if aula.disciplina.e_tecnica:

                        if not aula.sala.laboratorio:
                            return False

        return True
    
    def rr10_limite_aulas(self): # RR 10

        for dia in DIAS:

            if self.check_aulas_no_dia(dia) > 6:
                return False

        return True
    
    def rr11_check_noite_manha(self): # RR 11

        for dia in DIAS:
            for turno in TURNOS:
                for slot in TURNOS[turno]:
        
                    dia_atual = DIAS.index(dia)
                    
                    if self.check_noite_manha(dia_atual, turno, slot):
                        return False
                    
        return True

    # Restrições Flexíveis

    def rf1_quatro_aulas_seguidas(self):

        penalidade = 0

        for dia in DIAS:

            sequencia = 0
            ultima_turma = None

            ordem = [
                ("M", "AB"),
                ("M", "CD"),
                ("T", "AB"),
                ("T", "CD"),
            ]

            for turno, slot in ordem:

                aula = self.grade[dia][turno][slot]

                if aula is None:
                    sequencia = 0
                    ultima_turma = None
                    continue

                if turno == "N":
                    continue

                turma_atual = aula.turma.cod

                if turma_atual == ultima_turma:
                    sequencia += 1
                else:
                    sequencia = 1
                    ultima_turma = turma_atual

                if sequencia >= 2:
                    penalidade += 5

        return penalidade

    def rf2_mesma_turma_mesmo_professor(self):

        penalidade = 0

        for dia in DIAS:

            contador_turmas = {}

            for turno in ["M", "T"]: 

                for slot in TURNOS[turno]:

                    aula = self.grade[dia][turno][slot]

                    if aula is None:
                        continue

                    turma = aula.turma.cod

                    if turma not in contador_turmas:
                        contador_turmas[turma] = 0

                    contador_turmas[turma] += 1

            # verifica excesso
            for turma in contador_turmas:

                # 2 slots = 4 aulas/horas
                if contador_turmas[turma] >= 2:
                    penalidade += 1

        return penalidade
    
    def rf3_priorizar_inicio_fim_livre(self):

        penalidade = 0

        # apenas manhã e tarde
        ordem = [
            ("M", "AB"),
            ("M", "CD"),
            ("T", "AB"),
            ("T", "CD"),
        ]

        turmas = set()

        # pega todas as turmas existentes
        for dia in DIAS:
            for turno in ["M", "T"]:
                for slot in TURNOS[turno]:

                    aula = self.grade[dia][turno][slot]

                    if aula is not None:
                        turmas.add(aula.turma.cod)

        # analisa cada turma
        for turma in turmas:

            for dia in DIAS:

                ocupados = []

                for turno, slot in ordem:

                    aula = self.grade[dia][turno][slot]

                    if aula is not None and aula.turma.cod == turma:
                        ocupados.append(True)
                    else:
                        ocupados.append(False)

                primeira = -1
                ultima = -1

                for i in range(len(ocupados)):

                    if ocupados[i]:

                        if primeira == -1:
                            primeira = i

                        ultima = i

                # menos de duas aulas
                if primeira == -1 or primeira == ultima:
                    continue

                # conta buracos internos
                for i in range(primeira, ultima + 1):

                    if not ocupados[i]:
                        penalidade += 1

        return penalidade
    
    def rf4_priorizar_manha(self):

        penalidade = 0

        for dia in DIAS:

            for slot in TURNOS["T"]:

                aula = self.grade[dia]["T"][slot]

                if aula is not None:

                    penalidade +=1

        return penalidade

    def rf5_evitar_janelas(self):

        penalidade = 0

        ordem = [
            ("M", "AB"),
            ("M", "CD"),
            ("T", "AB"),
            ("T", "CD"),
            ("N", "AB"),
            ("N", "CD"),
        ]

        for dia in DIAS:

            ocupados = []

            for turno, slot in ordem:

                aula = self.grade[dia][turno][slot]

                ocupados.append(aula is not None)

            for i in range(1, len(ocupados)-1):

                if ocupados[i-1] and not ocupados[i] and ocupados[i+1]:
                    penalidade += 3

        return penalidade
    
    def rf6_concentrar_disciplinas(self):

        penalidade = 0

        salas_por_disciplina = {}

        for dia in DIAS:
            for turno in TURNOS:
                for slot in TURNOS[turno]:

                    aula = self.grade[dia][turno][slot]

                    if aula is None:
                        continue

                    disciplina = aula.disciplina.cod
                    sala = aula.sala.num_sala

                    if disciplina not in salas_por_disciplina:
                        salas_por_disciplina[disciplina] = set()

                    salas_por_disciplina[disciplina].add(sala)

        for disciplina in salas_por_disciplina:

            quantidade_salas = len(
                salas_por_disciplina[disciplina]
            )

            if quantidade_salas > 1:

                penalidade += (
                    quantidade_salas - 1
                )

        return penalidade


    # Funções Auxiliares:

    def check_horas_livres_minimas(self):

        bloqueados = self.professor.getHorarios_Bloqueados()

        slots_bloqueados = 0

        for dia, turno, slot in bloqueados:

            # conta apenas manhã e tarde
            if turno in ["M", "T"]:
                slots_bloqueados += 1

        horas_livres = 40 - (slots_bloqueados * 2)

        return horas_livres >= 20

    def horario_grade(self, dia, turno, slot):  # retorna um objeto do tipo Aula
        
        aula = self.grade[dia][turno][slot]
        if aula is None:
            print("Slot vazio\n")
        else:
            if aula.sala.laboratorio == True:
                print(f"Matéria: {aula.disciplina.nome}\nTurma: {aula.turma.cod}\nLaboratório: {aula.sala.num_sala}\n")
            else:
                print(f"Matéria: {aula.disciplina.nome}\nTurma: {aula.turma.cod}\nSala: {aula.sala.num_sala}\n")

    def get_indices_dias_utilizados(self):
        dias_utilizados = set()

        for i, dia in enumerate(DIAS):

            for turno in TURNOS:
                for slot in TURNOS[turno]:

                    if self.grade[dia][turno][slot] is not None:
                        dias_utilizados.add(i)

        return sorted(dias_utilizados)
    
    def check_dias_concentrados(self, dia):
    
        dias_utilizados = self.get_indices_dias_utilizados()

        # ainda não tem aulas
        if len(dias_utilizados) == 0:
            return True

        indice_novo = DIAS.index(dia)

        # adiciona o novo dia temporariamente
        todos = dias_utilizados + [indice_novo]
        todos = sorted(set(todos))

        # verifica buracos
        for i in range(len(todos) - 1):

            diferenca = todos[i + 1] - todos[i]

            # se houver buraco entre dias
            if diferenca > 1:
                return False

        return True

    def check_salas(self, dia, turno, slot, disciplina):
        salas_compativeis = []

        for sala in self.salas:

            # sala ocupada → ignora
            if sala.esta_ocupada(dia, turno, slot):
                continue

            # compatibilidade lab / não lab
            if sala.laboratorio == disciplina.e_tecnica:
                salas_compativeis.append(sala)

        return salas_compativeis

    def check_noite_manha(self, dia_atual, turno, slot):
        # Verifica se há aula de noite no dia anterior
        if turno == "M" and slot == "AB":
            if dia_atual == 0:
                pass
            else:
                dia_anterior = DIAS[dia_atual - 1]
                
                for slot in TURNOS["N"]:
                    if self.grade[dia_anterior]['N'][slot] is not None:
                        return True
        
        # Verifica se há aula de manhã no horário AB no próximo dia
        if turno == "N":
            if dia_atual < len(DIAS) - 1:
                dia_seguinte = DIAS[dia_atual + 1]

                # verifica se já existe M-AB no dia seguinte
                if self.grade[dia_seguinte]["M"]["AB"] is not None:
                    return True
        return False
    
    def check_aulas_no_dia(self, dia):
        total = 0

        for turno in TURNOS:
            for slot in TURNOS[turno]:
                if self.grade[dia][turno][slot] is not None:
                    total += 2

        return total
    
    def __repr__(self):

        if self.horario_valido == False:
            return f"O professor {self.professor} não possui o número mínimo de horários livres!"
        
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
