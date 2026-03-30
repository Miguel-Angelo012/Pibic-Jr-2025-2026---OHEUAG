from disciplina import Disciplina
from turma import Turma
from sala import Sala
from typing import Tuple

class Aula:

    def __init__(self,
                 alocacao = Tuple[Disciplina, Turma],
                 sala = Sala
                 ):
        
        self.alocacao = alocacao
        self.sala = sala

    def __repr__(self):

        aula = f"""
        Disciplina: {self.alocacao[0]}\n
        Turma: {self.alocacao[1]}
        Sala: {self.sala}
        """
        
        return aula
