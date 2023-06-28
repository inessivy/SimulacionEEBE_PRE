import pygame.sprite

from TodoAula.Suelo import Suelo
from TodoAula.Tarima import Tarima
from TodoAula.Puerta import Puerta
from TodoAula.MesaProf import MesaProf
from TodoAula.Mesa import Mesa
from TodoAula.Entrada import Entrada


IMG_DIR = "imagenesproy"


class Aula():
    def __init__(self, mx, my, filas, columnas):
        self.size = [(650, 742)]
        self.entrada = Entrada(635, 80)
        self.tarima = Tarima(IMG_DIR)
        self.mesas = pygame.sprite.Group()
        for n in range(columnas):
            for m in range(filas):
                self.mesas.add(Mesa(mx, my))
                my += 100
            mx = 350
            my = 210
        self.sillas = pygame.sprite.Group(i.sillas for i in self.mesas)
        self.ent_pasillos = pygame.sprite.Group()
        mx = 70
        for i in range(3):
            entrada_pas = Entrada(mx - 35, my - 50)
            self.ent_pasillos.add(entrada_pas)
            mx += 270
        self.ent_mesas = pygame.sprite.Group()
        for i in self.mesas:
            self.ent_mesas.add(i.entrada_izq, i.entrada_der)

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

    def get_ent_pasillos(self):
        return self.ent_pasillos.sprites()

    def get_ent_mesas(self, pasillo):
        if pasillo == self.get_ent_pasillos()[0]:
            return self.ent_mesas.sprites()[0:9:2]
        elif pasillo == self.get_ent_pasillos()[1]:
            return self.ent_mesas.sprites()[1:10:2] + self.ent_mesas.sprites()[10:20:2]
        else:
            return self.ent_mesas.sprites()[11:20:2]

    def get_pasillo(self, ent_mesa):
        if ent_mesa in self.ent_mesas.sprites()[0:9:2]:
            return self.get_ent_pasillos()[0]
        if ent_mesa in self.ent_mesas.sprites()[1:10:2]:
            return self.get_ent_pasillos()[1]
        else:
            return self.get_ent_pasillos()[2]

    def get_sillas_libres(self):
        sillas_libres = []
        for i in self.mesas:
            for j in i.sillas:
                if not j.ocupada():
                    sillas_libres.append(j)
        return sillas_libres
