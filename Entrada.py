import pygame.sprite, os

IMG_DIR = "imagenesproy"
class Entrada(pygame.sprite.Sprite):
    def __init__(self, x, y, dir_img = IMG_DIR):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(dir_img, "entrada.png")), (2, 2))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.destino = pygame.sprite.Sprite()

    # def dibuj_ent(self, pant, ent_pasillo):
    #     ent_pasillo(self)
    #     ent_pasillo.draw(pant)
