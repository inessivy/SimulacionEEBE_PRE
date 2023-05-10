from Suelo import Suelo
from Tarima import Tarima
from Puerta import Puerta
from MesaProf import MesaProf
from Mesa import Mesa

IMG_DIR = "imagenesproy"

class Aula():
    def __init__(self):
        self.size = []

    def dibuj_aula(self, pant, grupo_mesa, grupo_silla):
        suelo = Suelo(IMG_DIR)
        suelo.dibuj_suelo(pant)

        tarima = Tarima(IMG_DIR)
        tarima.dibuj_tarima(pant)

        puerta = Puerta()
        puerta.dibuj_puerta(pant)

        mesaprof = MesaProf(IMG_DIR)
        mesaprof.dibuj_mesa_prof(pant)

        mesa = Mesa(70, 210)
        mesa.dibuj_mesa(pant, grupo_mesa, grupo_silla)


