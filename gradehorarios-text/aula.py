from disciplina import Disciplina
from turma import Turma
from sala import Sala
from typing import Tuple

class Aula:

    def __init__(self,
                 alocacao = tuple[Disciplina, Turma],
                 sala = Sala
                 ):
        
        self.disciplina = alocacao[0]
        self.turma = alocacao[1]
        self.sala = sala

    def __repr__(self):

        return f"""
                {self.disciplina}\n
                {self.turma}\n
                {self.sala}\n"""
