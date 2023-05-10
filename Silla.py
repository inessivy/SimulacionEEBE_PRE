import pygame.sprite
import os

IMG_DIR = "imagenesproy"

class Silla(pygame.sprite.Sprite):
    def __init__(self, sx, sy, dir_img=IMG_DIR):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(dir_img, "Silla.jpg")), (20, 20))
        self.rect = self.image.get_rect()
        self.rect.left = sx
        self.rect.top = sy

    def dibuj_silla(self, pant, grupo):
        for i in range(4):
            self.add(grupo)
            self.rect.left += 30
        grupo.draw(pant)
