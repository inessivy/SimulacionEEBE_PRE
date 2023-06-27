import pygame
import random
import os
from TodoAula.Persona import Persona

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
        # self.dest =
        # self.dest = random.choice(self.space.sillas(ent_mesa))

        for i in self.space.mesas.sprites():
            if ent_mesa == i.entrada_der:
                self.dest = i.get_sillas(ent_mesa)[0]
                c = 0
                if not self.dest.ocupada:
                    self.dir = self.dest.rect.center
                    self.dest.ocupada = True
                    c += 1
                    print("OCUPO UNA SILLA")
                elif i.get_sillas(ent_mesa)[1].ocupada == False:
                    self.dest = i.get_sillas(ent_mesa)[1]
                    self.dir = self.dest.rect.center
                    self.dest.ocupada = True
                    c += 1
                    print("OCUPO LA SILLA DE AL LADO")
                else:
                    self.dest = ent_mesa
                    self.dir = self.dest.rect.center
                    print("NO TENGO SILLA")
                    if i.get_ocupacion() == True:
                        print(c, "MESA OCUPADA. NO TENGO SILLA")
            elif ent_mesa == i.entrada_izq:
                # print("SOY DE LA IZQUIERDA")
                # self.dest = random.choice(self.space.get_ent_pasillos())
                self.dest = self.space.get_ent_pasillos()[1]
                self.dir = self.dest.rect.center



            # mit = iter(self.space.ent_mesas.sprites())
            # c = 0
            # if ent_mesa == i.entrada_izq or ent_mesa == i.entrada_der:
            #     if not i.ocupada:
            #         if not self.dest.ocupada:
            #             self.dir = self.dest.rect.center
            #             self.dest.ocupada = True
            #             c += 1
            #             print("SILLA NO OCUPADA", c, ent_mesa.rect.center, self.dir)
            #         else:
            #             self.dest = next() # MIRAR LA SILLA DE AL LADO SI ESTA OCUPADA
            #             self.dir = self.dest.rect.center
            #             print("SILLA OCUPADA", self.dir)
            #     elif c == 4:
            #         i.ocupada = True
            #         print("MESA OCUPADA")
            #         self.dest = next(mit, ent_mesa)
            #         self.dir = self.dest.rect.center

        # for i in self.space.mesas.sprites():
        #     mit = iter(self.space.mesas.sprites())
        #     if ent_mesa == i.entrada_izq or ent_mesa == i.entrada_der:
        #         c = 0
        #         if not i.ocupada:
        #             if not self.dest.ocupada:
        #                 self.dir = self.dest.rect.center
        #                 self.dest.ocupada = True
        #                 print("SILLA NO OCUPADA")
        #                 c += 1
        #             else:
        #                 sit = iter(self.space.sillas(ent_mesa))
        #                 self.dest = next(sit)
        #                 self.dir = self.dest.rect.center
        #                 print("SILLA OCUPADA")
        #         elif c == 4:
        #             i.ocupada = True
        #             print("MESA OCUPADA")
        #             self.dest = next(mit, ent_mesa)
        #             self.dir = self.dest.rect.center