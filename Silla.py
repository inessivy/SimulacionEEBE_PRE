import pygame.sprite
import os

IMG_DIR = "imagenesproy"

class Silla(pygame.sprite.Sprite):
    def __init__(self, sx, sy, dir_img=IMG_DIR):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(dir_img, "Silla.jpg")), (40, 40))
        self.rect = self.image.get_rect()
        self.rect.left = sx
        self.rect.top = sy
        # self.rect.centerx = sx + 20
        # self.rect.centery = sy + 20
        self.ocupada = False

    def dibuj_silla(self, pant):
        pant.blit(self.image, (self.rect.left, self.rect.top))
