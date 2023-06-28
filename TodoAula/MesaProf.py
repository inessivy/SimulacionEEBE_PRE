import pygame
import os


class MesaProf():
    def __init__(self, dir_img, x=21.25, y=51.25):
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(dir_img, "MesaProf.jpg")), (78.75, 43.75))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

    def dibuj_mesa_prof(self, pant):
        pygame.draw.rect(pant, [0, 0, 0], (20, 50, 80, 45))
        pant.blit(self.image, (self.rect.left, self.rect.top))
