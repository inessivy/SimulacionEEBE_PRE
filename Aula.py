from Suelo import Suelo
from Tarima import Tarima
from Puerta import Puerta
from MesaProf import MesaProf
from Mesa import Mesa
from Silla import Silla


class Aula():
    def __init__(self):
        self.size = []

    #  tx=3, ty=5, mesx=70, mesy = 210
    def dibuj_aula(self, pant, grupo_mesa, grupo_silla):
        Suelo.dibuj_suelo(pant)
        Tarima.dibuj_tarima(pant)
        Puerta.dibuj_puerta(pant)
        MesaProf.dibuj_mesa_prof(pant)
        Mesa.dibuj_mesa(pant, grupo_mesa, grupo_silla)
