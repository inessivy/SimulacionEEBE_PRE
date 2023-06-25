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

    # sacar destino del aula y cambiar el destino
    def go_mesa(self, pasillo):
        self.dest = random.choice(self.space.get_ent_mesas(pasillo))
        self.dir = self.dest.rect.center

    def go_silla(self, ent_mesa):
        self.speedx = 1
        self.speedy = 1
        for i in self.space.mesas.sprites():
            if ent_mesa == i.entrada_der or ent_mesa == i.entrada_izq:
                self.dest = i.get_sillas(ent_mesa)[0]
                c = 0
                if not self.dest.ocupada():
                    self.dir = self.dest.rect.center
                    self.dest.sentar(self)
                    c += 1
                    print("OCUPO UNA SILLA")
                elif not i.get_sillas(ent_mesa)[1].ocupada():
                    self.dest = i.get_sillas(ent_mesa)[1]
                    self.dir = self.dest.rect.center
                    self.dest.sentar(self)
                    c += 1
                    print("OCUPO LA SILLA DE AL LADO")
                elif i.get_ocupacion():
                    print(c, "MESA OCUPADA. NO TENGO SILLA")
                    self.dest = random.choice(self.space.get_ent_pasillos())
                    self.dir = self.dest.rect.center
                # else:
                #     self.dest = random.choice(self.space.get_ent_pasillos())
                #     self.dir = self.dest.rect.center
                #     print("NO TENGO SILLA")
                #     if i.get_ocupacion() == True:
                #         print(c, "MESA OCUPADA. NO TENGO SILLA")


    def find_new_mesa(self):
        pass
        # preguntar que mesa no esta ocupada, solo necesita que tenga 1 libre

