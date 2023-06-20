import pygame.sprite

from Suelo import Suelo
from Tarima import Tarima
from Puerta import Puerta
from MesaProf import MesaProf
from Mesa import Mesa
from Entrada import Entrada


IMG_DIR = "imagenesproy"

class Aula():
    def __init__(self, mx, my, filas, columnas): #mx=70, my=210
        self.size = [(650, 742)]
        self.mesas = pygame.sprite.Group()
        for n in range(columnas):
            for n in range(filas):
                self.mesas.add(Mesa(mx, my))
                my += 100
            mx = 350
            my = 210

        self.ent_pasillos = pygame.sprite.Group()
        mx = 70
        for i in range(3):
            entrada_pas = Entrada(mx-35, my-50)
            self.ent_pasillos.add(entrada_pas)
            mx += 270

        self.ent_mesas = pygame.sprite.Group()
        for i in self.mesas:
            ent_izq_mesa = Entrada(i.rect.left-30, i.rect.bottom+20)
            ent_der_mesa = Entrada(i.rect.right+30, i.rect.bottom+20)
            self.ent_mesas.add(ent_izq_mesa, ent_der_mesa)


    def dibuj_aula(self, pant):
        suelo = Suelo(IMG_DIR)
        suelo.dibuj_suelo(pant)

        tarima = Tarima(IMG_DIR)
        tarima.dibuj_tarima(pant)

        puerta = Puerta()
        puerta.dibuj_puerta(pant)

        mesaprof = MesaProf(IMG_DIR)
        mesaprof.dibuj_mesa_prof(pant)

        for m in self.mesas:
            m.dibuj_mesa(pant)

        self.ent_pasillos.draw(pant)

        self.ent_mesas.draw(pant)
