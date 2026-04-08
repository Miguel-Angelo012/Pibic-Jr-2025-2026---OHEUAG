class Sala:

    def __init__(self,
                 num_sala : int,
                 capacidade : int,
                 laboratorio : bool
                 ):
                 
        self.num_sala = num_sala
        self.capacidade = capacidade
        self.laboratorio = laboratorio
        self.ocupacao = {}

    def esta_ocupada(self, dia, turno, slot):
        return self.ocupacao.get((dia, turno, slot), False)

    def ocupar(self, dia, turno, slot):
        self.ocupacao[(dia, turno, slot)] = True

    def __repr__(self):
        return f"Sala {self.num_sala}"
