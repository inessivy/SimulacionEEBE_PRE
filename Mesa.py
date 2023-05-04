import pygame.sprite


class Mesa(pygame.sprite.Sprite):
    def __init__(self, x, y, imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y




