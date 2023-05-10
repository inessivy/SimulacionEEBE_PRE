import pygame.sprite
import os
from Silla import Silla

IMG_DIR = "imagenesproy"


class Mesa(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "mesa.jpg")), (198.75, 43.75))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y



    def dibuj_mesa(self, pant, grupo_mesa, grupo_silla):
        # Dibujo el marco de la mesa y dibujo los sprites del grupo. Dibujo las sillas
        pygame.draw.rect(pant, [0, 0, 0], (self.rect.left - 1.25, self.rect.top - 1.25, 200, 45))
        for j in range(2):
            for i in range(5):
                self.add(grupo_mesa)
            self.rect.top += 100
            self.rect.top = 210
            self.rect.left = 350
        grupo_mesa.draw(pant)

        # sillas
        for i in range(4):
            silla = Silla(65, 250)
        silla.dibuj_silla(pant, grupo_silla)
