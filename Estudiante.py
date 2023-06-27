import pygame
import random
import os
from Persona import Persona

IMG_DIR = "imagenesproy"


class Estudiante(Persona):
    def __init__(self, x, y, espacio):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, random.choice(["mujer_caminando.png", "hombre_caminando.png"]))), (45, 60))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedx = random.uniform(1, 3)
        self.speedy = random.uniform(1, 3)
        self.space = espacio
        # self.space.create_ent_pasillos()
        self.dest = random.choice(self.space.get_ent_pasillos())
        self.dir = self.dest.rect.center

    def change_image(self):
        # if self.rect.center == self.dir:
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, random.choice(["mujer_sentada.png", "hombre_sentado.png"]))), (45, 60))
        # if self.image == pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "mujer_caminando.png")), (50, 50)):
        #     self.image = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "mujer_sentada.png")), (50, 50))
        # else:
        #     self.image = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "hombre_sentado.png")), (50, 50))

    def find_new_silla(self):
        # preguntar que mesa no esta ocupada, solo necesita que tenga 1 libre
        new_silla = self.space.get_sillas_libres()
        return new_silla

    def go_new_silla(self):
        new_silla = random.choice(self.find_new_silla())
        print("nueva silla", new_silla)
        if self.rect.center == self.space.get_pasillo(new_silla.entrada):
            print("voy a nueva mesa")
            self.dest = new_silla.entrada
            self.dir = self.dest.rect.center
        elif self.rect.center == new_silla.entrada:
            print("voy a nueva silla")
            self.dest = new_silla
            self.dir = self.dest.rect.center
            self.dest.sentar(self)
            self.space.estudiantes_sentados.add(self)
        else:
            print("salgo al pasillo")
            self.dest = self.space.get_pasillo(new_silla.entrada)
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
                if not self.dest.ocupada(): # la primera
                    print("primera silla")
                    self.dir = self.dest.rect.center
                    self.dest.sentar(self)
                    self.space.estudiantes_sentados.add(self)

                elif not i.get_sillas(ent_mesa)[1].ocupada():   # la silla del lado
                    print("segunda silla")
                    self.dest = i.get_sillas(ent_mesa)[1]
                    self.dir = self.dest.rect.center
                    self.dest.sentar(self)
                    self.space.estudiantes_sentados.add(self)
                elif ent_mesa.destino.get_ocupacion(ent_mesa) and not all([w.destino.get_ocupacion(w) for w in self.space.get_ent_mesas(self.pasillo)]):
                    print("busco otra mesa")
                    # busco una silla en mismo pasillo
                    for j in self.space.get_ent_mesas(self.pasillo):
                        if not j.destino.get_ocupacion(j):
                            self.dest = j
                            self.dir = self.dest.rect.center
                # if all([w.destino.get_ocupacion(w) for w in self.space.get_ent_mesas(self.pasillo)]):
                else:
                    # print("voy al pasillo")
                    # busco silla en otro pasillo
                    if self.rect.center == self.space.get_ent_mesas(self.pasillo)[0].rect.center:
                        print("busco silla en otro pasillo")
                        self.go_new_silla()
                    else:
                        self.dest = self.space.get_ent_mesas(self.pasillo)[0]
                        self.dir = self.dest.rect.center
        if self.rect.center == self.dir:
            self.change_image()

