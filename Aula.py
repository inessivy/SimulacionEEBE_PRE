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
        # self.columnas_mesas = columnas
        # self.filas_mesas= filas
        # self.mesas_x = mx
        # self.mesas_y = my
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
            entrada_pas = Entrada(mx - 35, my - 50)
            self.ent_pasillos.add(entrada_pas)
            mx += 270
        self.ent_mesas = pygame.sprite.Group()
        for i in self.mesas:
            self.ent_mesas.add(i.entrada_izq, i.entrada_der)

        self.estudiantes_sentados = pygame.sprite.Group()

    # def create_matrix_mesas(self):
    #     for n in range(self.columnas_mesas):
    #         for n in range(self.filas_mesas):
    #             self.mesas.add(Mesa(self.mesas_x, self.mesas_y))
    #             self.mesas_y += 100
    #         self.mesas_x = 350
    #         self.mesas_y = 210

    # def create_ent_pasillos(self):
    #     self.mesas_x = 70
    #     for i in range(3):
    #         entrada_pas = Entrada(self.mesas_x - 35, self.mesas_y - 50)
    #         self.ent_pasillos.add(entrada_pas)
    #         self.mesas_x += 270

    # def create_ent_mesas(self):
    #     for i in self.mesas:
    #         self.ent_mesas.add(i.entrada_izq, i.entrada_der)


    def dibuj_aula(self, pant):
        suelo = Suelo(IMG_DIR)
        suelo.dibuj_suelo(pant)

        tarima = Tarima(IMG_DIR)
        tarima.dibuj_tarima(pant)

        puerta = Puerta()
        puerta.dibuj_puerta(pant)

        mesaprof = MesaProf(IMG_DIR)
        mesaprof.dibuj_mesa_prof(pant)

        # self.create_matrix_mesas()
        for m in self.mesas:
            m.dibuj_mesa(pant)
        # self.create_ent_pasillos()
        self.ent_pasillos.draw(pant)
        # self.create_ent_mesas()
        self.ent_mesas.draw(pant)

    #  metodos para devolder diferentes destinos(pasillo, mesa, silla)
    def get_ent_pasillos(self):
        return self.ent_pasillos.sprites()

    def get_ent_mesas(self, pasillo):
        if pasillo == self.get_ent_pasillos()[0]:
            return self.ent_mesas.sprites()[0:9:2]
        elif pasillo == self.get_ent_pasillos()[1]:
            return self.ent_mesas.sprites()[1:10:2] + self.ent_mesas.sprites()[10:20:2]
        else:
            return self.ent_mesas.sprites()[11:20:2]

    def get_mesas_libres(self):
        mesas_libres = []
        for i in self.mesas:
            if not i.get_ocupacion(i.entrada_izq) or not i.get_ocupacion(i.entrada_der):
                mesas_libres.append(i)

    def get_sillas_libres(self, mesa):
        sillas_libres = []
        for i in mesa.sillas:
            if not i.ocupada():
                sillas_libres.append(i)
        return sillas_libres


    # def get_ocupacion_mesa(self, mesa):
    #     return mesa.get_ocupacion()


