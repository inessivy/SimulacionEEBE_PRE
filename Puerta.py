import pygame
class Puerta():
    def __init__(self):
        pass
    def dibuj_puerta(self, pant):
        self.image = pygame.draw.rect(pant, [150, 105, 25], (695, 50, 5, 100))
