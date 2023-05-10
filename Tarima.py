import pygame, os
class Tarima():
    def __init__(self, tx, ty, dir_img):
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(dir_img, "suelo azul.jpg")), (30, 48))
        self.rect = self.image.get_rect()
        self.rect.left = tx
        self.rect.top = ty

    def dibuj_tarima(self, pant):
        pygame.draw.rect(pant, [0, 0, 0], (5, 5, 540, 98))
        for i in range(2):
            for j in range(18):
                pant.blit(self.image, (self.rect.left, self.rect.top))
                self.rect.left += 30
            self.rect.left = 3
            self.rect.top += 48
