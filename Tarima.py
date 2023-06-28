import pygame
from Entrada import *


class Tarima():
    def __init__(self, dir_img, tx=3, ty=2):
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(dir_img, "suelo azul.jpg")), (30, 48))
        self.rect = self.image.get_rect()
        self.rect.left = tx
        self.rect.top = ty
        self.entrada = Entrada(272, 50)
        self.p_izq = Entrada(self.entrada.rect.centerx - 100, 50)
        self.p_der = Entrada(self.entrada.rect.centerx + 100, 50)

    def get_entradas(self):
        return pygame.sprite.Group([self.entrada, self.p_der, self.p_izq])

    def dibuj_tarima(self, pant):
        pygame.draw.rect(pant, [0, 0, 0], (0, 0, 545, 100))
        for i in range(2):
            for j in range(18):
                pant.blit(self.image, (self.rect.left, self.rect.top))
                self.rect.left += 30
            self.rect.left = 3
            self.rect.top += 48
