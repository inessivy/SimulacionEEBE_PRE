import pygame
import random
import os
from TodoAula.Persona import Persona

IMG_DIR = "imagenesproy"


class Estudiante(Persona):
    def __init__(self, x, y, espacio):
        pygame.sprite.Sprite.__init__(self)
        self.imagenes = {"hombre": {"sentado": "hombre_sentado.png", "andando": "hombre_caminando.png"},
                         "mujer": {"sentado": "mujer_sentada.png", "andando": "mujer_caminando.png"}}
        self.sexo = random.choice(list(self.imagenes))
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(
            IMG_DIR, self.imagenes[self.sexo]["andando"])), (45, 60))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedx = random.uniform(1, 3)
        self.speedy = random.uniform(1, 3)
        self.space = espacio
        self.dest = random.choice(self.space.get_ent_pasillos())
        self.dir = self.dest.rect.center

    def salir(self):
        if self.dest.estudiante is None:
            if self.dest in self.space.get_ent_pasillos():
                self.dest = self.space.entrada
                self.dir = self.dest.rect.center
            elif self.rect.center == self.dest.entrada.rect.center:
                self.dest = self.space.get_pasillo(self.dest)
                self.dir = self.dest.rect.center
            elif self.rect.center == self.dir:
                self.dest = self.dest.entrada
                self.dir = self.dest.rect.center

    def sentado(self):
        if self.rect.center == self.dir:
            self.image = pygame.transform.scale(
                pygame.image.load(os.path.join(IMG_DIR, self.imagenes[self.sexo]["sentado"])), (45, 60))

    def find_new_silla(self):
        new_silla = self.space.get_sillas_libres()
        return new_silla

    def go_new_silla(self):
        new_silla = random.choice(self.find_new_silla())
        if self.rect.center == self.space.get_pasillo(new_silla.entrada):
            self.dest = new_silla.entrada
            self.dir = self.dest.rect.center
        elif self.rect.center == new_silla.entrada:
            self.dest = new_silla
            self.escoger_silla(self.dest)

        else:
            self.dest = self.space.get_pasillo(new_silla.entrada)
            self.dir = self.dest.rect.center

    def go_mesa(self, pasillo):
        self.pasillo = pasillo
        self.speedx = 1
        self.speedy = 1
        self.dest = random.choice(self.space.get_ent_mesas(pasillo))
        self.dir = self.dest.rect.center

    def escoger_silla(self, dest):
        self.dir = dest.rect.center
        self.dest.sentar(self)

    def go_silla(self, ent_mesa):
        self.speedx = 1
        self.speedy = 1
        for i in self.space.mesas.sprites():
            if ent_mesa == i.entrada_der or ent_mesa == i.entrada_izq:
                self.dest = i.get_sillas(ent_mesa)[0]
                if not self.dest.ocupada():
                    self.escoger_silla(self.dest)

                elif not i.get_sillas(ent_mesa)[1].ocupada():
                    self.dest = i.get_sillas(ent_mesa)[1]
                    self.escoger_silla(self.dest)

                elif ent_mesa.destino.get_ocupacion(ent_mesa) and not all(
                        [w.destino.get_ocupacion(w) for w in self.space.get_ent_mesas(self.pasillo)]):
                    for j in self.space.get_ent_mesas(self.pasillo):
                        if not j.destino.get_ocupacion(j):
                            self.dest = j
                            self.dir = self.dest.rect.center
                else:
                    if self.rect.center == self.space.get_ent_mesas(self.pasillo)[0].rect.center:
                        self.go_new_silla()
                    else:
                        self.dest = self.space.get_ent_mesas(self.pasillo)[0]
                        self.dir = self.dest.rect.center
