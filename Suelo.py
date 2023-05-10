import pygame
import os
class Suelo():
    def __init__(self, slx, sly, dir_img):
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(dir_img, "suelo2.png")), (52, 60))
        self.rect = self.image.get_rect()
        self.left = slx
        self.top = sly

    def dibuj_suelo(self, pant):
        for i in range(12):
            for j in range(12):
                pant.blit(self.image, (self.left, self.top))
                self.rect.left += 53
            self.rect.top += 61
            self.rect.left = 0