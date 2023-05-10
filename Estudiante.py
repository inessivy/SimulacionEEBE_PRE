import pygame
import random
import os
from Persona import Persona

IMG_DIR = "imagenesproy"

class Estudiante(Persona):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "estudiante.png")), (60, 60))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

    def destinos(self, x, y):
        DES = []
        for i in range(5):
            for j in range(4):
                if j == 0:
                    des = (x, y)
                else:
                    des = (DES[j - 1][0] + 50, y)
                DES.append(des)
            y += 100
        for i in range(5):
            for j in range(4):
                if j == 0:
                    des = (350, y - 500)
                else:
                    des = (DES[-1][0] + 50, y - 500)
                DES.append(des)
            y += 100
        return DES

    def dibuj_estudiante(self, pant, grupo_est):      # x=600 y=80
        # for i in range(random.randint(1, 40)):
        for i in range(1):
            global DEST
            DEST = self.destinos(65, 250)
            self.dir = random.choice(DEST)
            DEST.remove(self.dir)
            self.speedx = random.uniform(1, 3)
            self.speedy = random.uniform(1, 3)
            self.add(grupo_est)
        grupo_est.draw(pant)
    def gestion_colision(self, sprite1, sprite2):
        """
        To use the collided argument, you need to define a callback function
        that accepts two arguments representing the collided sprites.
        The collided function will be called for each pair of collided sprites.
        """
        print("Colision entre", sprite1, "y", sprite2)
        self.dir = random.choice(DEST)
