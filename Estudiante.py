import random, pygame


class Estudiante(pygame.sprite.Sprite):
    def __init__(self, x, y, imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.dirx = random.randrange(650)
        self.diry = random.randrange(742)
        self.speed = 3

    def update(self):
        if self.rect.centerx >= self.dirx:
            self.rect.centerx -= self.speed
        if self.rect.centery <= self.diry:
            self.rect.centery += self.speed


    def parar(self):
        pass
