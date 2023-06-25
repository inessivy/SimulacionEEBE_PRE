import random
import pygame.sprite


class Persona(pygame.sprite.Sprite):
    def __init__(self, x, y, imagen=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.dir = [random.randrange(650), random.randrange(742)]
        self.speedx = 3.4
        self.speedy = 3.4

    def update(self):
        if self.rect.centerx - self.dir[0] > 0:
            self.rect.centerx -= self.speedx
        elif self.rect.centerx - self.dir[0] < 0:
            self.rect.centerx += self.speedx
        else:
            pass
        if self.rect.centery - self.dir[1] < 0:
            self.rect.centery += self.speedy
        elif self.rect.centery - self.dir[1] > 0:
            self.rect.centery -= self.speedy
        else:
            pass

        # if self.rect.centerx > self.dir[0]:
        #     self.rect.centerx -= self.speedx
        # elif self.rect.centerx < self.dir[0]:
        #     self.rect.centerx += self.speedx
        #     print(self.rect.center, self.dir)
        #     # print(self.rect.center)
        # if self.rect.centery < self.dir[1]:
        #     self.rect.centery += self.speedy
        # elif self.rect.centery > self.dir[1]:
        #     self.rect.centery -= self.speedy
        #     print(self.rect.center, self.dir)
