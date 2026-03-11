class Professor:

    def __init__(self, matricula : int, nome : str):
        self.matricula = matricula
        self.nome = nome
        self.horarios = None
        self.horarios_bloqueados = None
        self.dias_concentrados = None

    def setHorarios(self, horarios : list):
        self.horarios = horarios

    def setHorarios_bloqueados(self, horarios_bloqueados : list):
        self.horarios_bloqueados = horarios_bloqueados

    def setDias_concentrados(self, dias_concentrados : bool):
        self.dias_concentrados = dias_concentrados



    