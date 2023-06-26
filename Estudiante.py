import pygame
import random
import os
from Persona import Persona

IMG_DIR = "imagenesproy"


class Estudiante(Persona):
    def __init__(self, x, y, aula):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "estudiante.png")), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedx = random.uniform(1, 3)
        self.speedy = random.uniform(1, 3)
        self.space = aula
        # self.space.create_ent_pasillos()
        self.dest = random.choice(self.space.get_ent_pasillos())
        self.dir = self.dest.rect.center


    # def find_new_silla(self):
    #     # preguntar que mesa no esta ocupada, solo necesita que tenga 1 libre
    #     new_mesa = random.choice(self.space.get_mesas_libres())
    #     new_silla = self.space.get_sillas_libres(new_mesa)
    #     return new_silla, new_mesa

    def go_new_silla(self):
        # new_mesa = self.find_new_silla()[1]
        new_mesa = random.choice(self.space.get_mesas_libres())
        # new_silla = self.find_new_silla()[0]
        # new_silla = self.space.get_sillas_libres(new_mesa)
        # ent_silla = new_mesa.get_ent_silla(new_silla)

        self.dest = new_mesa.entrada_izq
        self.dir = self.dest.rect.center



    # sacar destino del aula y cambiar el destino
    def go_mesa(self, pasillo):
        self.pasillo = pasillo
        self.speedx = 1
        self.speedy = 1
        self.dest = random.choice(self.space.get_ent_mesas(pasillo))
        self.dir = self.dest.rect.center

    def go_silla(self, ent_mesa):
        # para que no vibre
        self.speedx = 1
        self.speedy = 1
        # escojo silla
        for i in self.space.mesas.sprites():
            if ent_mesa == i.entrada_der or ent_mesa == i.entrada_izq:
                self.dest = i.get_sillas(ent_mesa)[0]
                if not self.dest.ocupada(): # la primera silla
                    self.dir = self.dest.rect.center
                    self.dest.sentar(self)

                elif not i.get_sillas(ent_mesa)[1].ocupada():   # la silla del lado
                    self.dest = i.get_sillas(ent_mesa)[1]
                    self.dir = self.dest.rect.center
                    self.dest.sentar(self)

                # elif self.dest not in self.space.ent_pasillos: # la silla no ha salido del pasillo
                elif ent_mesa.destino.get_ocupacion(ent_mesa) and not all(w.destino.get_ocupacion(w) for w in self.space.get_ent_mesas(self.pasillo)):
                    # busco una silla en mismo pasillo
                    print("hola")
                    for j in self.space.get_ent_mesas(self.pasillo):
                        if not j.destino.get_ocupacion(j):
                            self.dest = j
                            self.dir = self.dest.rect.center
                elif all(w.destino.get_ocupacion(w) for w in self.space.get_ent_mesas(self.pasillo)):
                # else:
                    # busco silla en otro pasillo
                    # if self.dir in [q.rect.center for q in self.space.get_ent_pasillos()]:
                    if self.rect.center == self.pasillo.rect.center:
                        print("busco silla en otro pasillo")
                        self.go_new_silla()
                    else:
                        self.dest = self.pasillo
                        self.dir = self.dest.rect.center
