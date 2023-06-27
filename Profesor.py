from Persona import *
import os
import time

IMG_DIR = "imagenesproy"

class Profesor(Persona):
    def __init__(self, x, y, espacio):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join(IMG_DIR, "profesor_caminando-png")),
            (50, 50))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedx = random.uniform(1, 3)
        self.speedy = random.uniform(1, 3)
        self.space = espacio
        self.dest = espacio.tarima
        self.dir = self.dest.rect.center

    def explicar(self):
        self.dir += 100
        pygame.time.wait(1000)
        self.dir -= 200
        pygame.time.wait(1000)
        self.dir += 100

