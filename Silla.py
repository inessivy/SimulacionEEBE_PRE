import pygame.sprite, os
class Silla(pygame.sprite.Sprite):
    def __init__(self, sx, sy, dir_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(dir_img, "Silla.jpg")), (20, 20))
        self.rect = self.image.get_rect()
        self.x = sx
        self.y = sy
    def add_grupo(self, grupo):
        self.add(grupo)
    def dibuj_silla(self, pant, grupo):
        grupo.draw(pant)
