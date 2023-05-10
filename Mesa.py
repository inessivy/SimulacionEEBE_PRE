import pygame.sprite, os
from Silla import Silla

class Mesa(pygame.sprite.Sprite):
    def __init__(self, x, y, dir_img): # x = 70, y = 210
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(dir_img, "mesa.jpg")), (198.75, 43.75))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
    def add_grupo(self, grupo):
        "Añado la mesa a un grupo"
        self.add(grupo)
    def dibuj_mesa(self, pant, grupo, grupo_silla):
        "Dibujo el marco de la mesa y dibujo los sprites del grupo. Dibujo las sillas"
        pygame.draw.rect(pant, [0, 0, 0], (self.rect.left - 1.25, self.rect.top - 1.25, 200, 45))
        grupo.draw(pant)
        # sillas
        msx = self.rect.left + 175
        for i in range(1):
            Silla.dibuj_silla(pant, grupo_silla)
            msx -= 50
