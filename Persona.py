import random
import pygame.sprite


class Persona(pygame.sprite.Sprite):
    def __init__(self, x, y, imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.dir = [random.randrange(650), random.randrange(742)]
        self.speedx = 3.4
        self.speedy = 3.4

    def update(self):
        if self.rect.left >= self.dir[0]:
            self.rect.left -= self.speedx
        if self.rect.top <= self.dir[1]:
            self.rect.top += self.speedy

    def colision(self):
        pass
