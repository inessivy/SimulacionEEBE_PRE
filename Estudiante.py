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
        self.dest = []
        for e in aula.ent_pasillos:
            self.dest.append([e.rect.centerx, e.rect.centery])

        list_sprites = pygame.sprite.Group.sprites(self.space.ent_mesas)
        for d in range(len(self.dest)):
                if d == 0:
                    for m in list_sprites[0:10:2]:
                        self.dest[d].append([m.rect.centerx, m.rect.centery])
                elif d == 1:
                    for m in list_sprites[1:10:2]:
                        self.dest[d].append([m.rect.centerx, m.rect.centery])
                    for m in list_sprites[10:19:2]:
                        self.dest[d].append([m.rect.centerx, m.rect.centery])
                else:
                    for m in list_sprites[11:20:2]:
                        self.dest[d].append([m.rect.centerx, m.rect.centery])

        list_sprites_sillas = []
        for m in aula.mesas:
            for s in m.sillas:
                list_sprites_sillas.append((s.rect.centerx, s.rect.centery))
        # CAMBIAR LINEAS 45:54 | SE NECESITA USAR LA LISTA SIN ELIMINAR NADA
        for i in range(3):
            if i == 0:
                for j in range(2,7):
                    self.dest[i][j].extend(list_sprites_sillas[0:20][slice(4)])
                    del list_sprites_sillas[0:4]
            if i == 1:
                for j in range(2,12):
                    self.dest[i][j].extend(list_sprites_sillas[0:20][slice(4)])
                    del list_sprites_sillas[0:4]
            if i == 2:
                for j in range(2,7):
                    self.dest[i][j].extend(list_sprites_sillas[0:20][slice(4)])
                    del list_sprites_sillas[0:4]



    def cambio_destino(self):
        collided_pas_list = pygame.sprite.spritecollide(self, self.space.ent_pasillos, False)
        for i in collided_pas_list:
            print(self.dest)
            print()

            # if i.rect.centerx == self.dir[0]:
            #     if i.rect.centerx == 35:
            #         self.dir = random.choice(self.dest[0][2])
            #         spr_ran = random.choice(self.space.mesas)
            #         self.dir = spr_ran.center
            #     if i.rect.centerx == 305:
            #         self.dir = random.choice(self.dest[1][2])
            #     if i.rect.centerx == 575:
            #         self.dir = random.choice(self.dest[2][2])
        collided_mesa_list_ = pygame.sprite.spritecollide(self, self.space.ent_mesas, False)
        for j in collided_mesa_list_:
            if j.rect.centery == self.dir[1]:
                pass


    def gestion_colision_mesa(self, sprite1, sprite2):
        """
        To use the collided argument, you need to define a callback function
        that accepts two arguments representing the collided sprites.
        The collided function will be called for each pair of collided sprites.
        """
        print("Colision entre", sprite1, "y", sprite2)
        if sprite1.rect.colliderect(sprite2.rect) == True:
            return True
    def gestion_colision_silla(self, sprite1, sprite2):
        """
        To use the collided argument, you need to define a callback function
        that accepts two arguments representing the collided sprites.
        The collided function will be called for each pair of collided sprites.
        """
        # print("Colision entre", sprite1, "y", sprite2)
        if sprite1.rect.centerx == sprite2.rect.centerx and sprite1.rect.centery == sprite2.rect.centery:
            if sprite1.dir == (sprite2.rect.centerx, sprite2.rect.centery):
                sprite1.speedx = 0
                sprite1.speedy = 0
            else:
                sprite1.rect.centerx = 600
                sprite1.rect.centery = 80

    # def gestion_colision_tarima(self, sprite1, sprite2):
    #     """
    #     To use the collided argument, you need to define a callback function
    #     that accepts two arguments representing the collided sprites.
    #     The collided function will be called for each pair of collided sprites.
    #     """
    #     print("Colision entre", sprite1, "y", sprite2)
    #     # RANDOM
    #     if sprite1.rect.top == sprite2.rect.bottom:
    #         # sprite1.speedx = 0
    #         sprite1.speedy += -1
