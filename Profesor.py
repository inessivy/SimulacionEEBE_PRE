from Persona import *
import os
import time

IMG_DIR = "imagenesproy"

class Profesor(Persona):
    def __init__(self, x, y, espacio):
        pygame.sprite.Sprite.__init__(self)
        # self.SONIDO_DIR = "sonidos proy"
        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join(IMG_DIR, "profesor_caminando.png")),
            (50, 50))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedx = random.uniform(1, 2)
        self.speedy = random.uniform(1, 2)
        self.space = espacio
        self.dest = self.space.tarima.entrada
        self.dir = self.dest.rect.center
        # self.sound = pygame.mixer.Sound(os.path.join(self.SONIDO_DIR, "fast_talking.mp3"))


    def explicar(self):
        # escoger un punto aleatorio
        # self.sound.play()
        # self.sound.set_volume(0.5)
        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join(IMG_DIR, "profesor_explicando.png")),
            (50, 50))
        self.speedx = 1
        self.dest = random.choice(list(self.space.tarima.get_entradas()))
        self.dir = self.dest.rect.center




