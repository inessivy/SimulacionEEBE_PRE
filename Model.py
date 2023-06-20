import pygame.sprite
from View_Aula import View

view = View()
class Model(object):
    def __init__(self):
        super().__init__()
        self.pos_aula = view.place.ent_pasillos.sprites()

    def quitar_sonido(self):
        pass

    def pausar_simul(self):
        pass




        # for e in view.estudiantes:
        #     for c in view.place.ent_pasillos:
        #         if e.rect.centerx == view.place.ent_pasillos[c].x and e.rect.centery == view.place.ent_pasillos[c].y:
        #             e.speedx = 0
        #             e.speedy = 0
        # self.ent_mesas = mesas.sprites()
        # self.sillas =
        # mesas = pygame.sprite.Group()  # falta añadir el punto de entrada(sprite) para cada mesa en Aula
        # for j in range(5):
        #     self.ent_pasillo.append(self.ent_mesa[j])
        #     for k in range(4):
        #         self.ent_mesa.append(self.sillas[k])


