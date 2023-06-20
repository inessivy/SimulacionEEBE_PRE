import pygame.sprite
import os
from Silla import Silla

IMG_DIR = "imagenesproy"


class Mesa(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """
        >>> m = Mesa(0, 0)

        :param x:
        :param y:
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "mesa.jpg")), (198.75, 43.75))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.sillas = pygame.sprite.Group()
        for n in range(4):
            self.sillas.add(Silla(x+5, y+45))
            x += 50

    def dibuj_mesa(self, pant):
        # pygame.draw.rect(pant, [0, 0, 0], (self.rect.left - 1.25, self.rect.top - 1.25, 300, 45))
        for s in self.sillas:
            s.dibuj_silla(pant)
        pant.blit(self.image, (self.rect.left, self.rect.top))


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())