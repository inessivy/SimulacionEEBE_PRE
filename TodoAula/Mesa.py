import pygame.sprite
import os
from TodoAula.Silla import Silla
from TodoAula.Entrada import Entrada

IMG_DIR = "imagenesproy"


class Mesa(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "mesa.jpg")), (198.75, 43.75))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.entrada_izq = Entrada(self.rect.left-30, self.rect.bottom+20)
        self.entrada_der = Entrada(self.rect.right+30, self.rect.bottom+20)
        self.entrada_izq.destino = self
        self.entrada_der.destino = self
        self.sillas = pygame.sprite.Group()
        for n in range(4):
            self.sillas.add(Silla(x+5, y+45))
            x += 50
        self.ocupada = False

    def dibuj_mesa(self, pant):
        for s in self.sillas:
            s.dibuj_silla(pant)
        pant.blit(self.image, (self.rect.left, self.rect.top))

    def get_sillas(self, ent_mesa):
        if ent_mesa == self.entrada_izq:
            for i in self.sillas.sprites()[0:2]:
                i.entrada = self.entrada_izq
            return self.sillas.sprites()[0:2]
        elif ent_mesa == self.entrada_der:
            for i in self.sillas.sprites()[2:]:
                i.entrada = self.entrada_der
            return self.sillas.sprites()[2:]

    def get_ocupacion(self, ent_mesa):
        ocupacion = [s.ocupada() for s in self.get_sillas(ent_mesa)]
        return all(ocupacion)


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
