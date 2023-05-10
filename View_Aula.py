import pygame
import sys
import random
from Aula import Aula
from Estudiante import Estudiante


class View():
    def __init__(self):
        self.size = (650, 742)
        self.SONIDO_DIR = "sonidos proy"


    def main(self):
        import time
        pygame.init()
        screen = pygame.display.set_mode(self.size)
        clock = pygame.time.Clock()
        sillagrup = pygame.sprite.Group()
        mesagrup = pygame.sprite.Group()
        estgrup = pygame.sprite.Group()
        aula = Aula()

        estudiante = Estudiante(600, 80)

        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # controles
            est = pygame.sprite.Group.sprites(estgrup)
            scollision_dict = pygame.sprite.groupcollide(estgrup, sillagrup, False, False,
                                                         collided=estudiante.gestion_colision)
            mcollision_dict = pygame.sprite.groupcollide(estgrup, mesagrup, False, False,
                                                         collided=estudiante.gestion_colision)
            for i in estgrup:
                i.update()

            # dibujar aula y estudiantes
            aula.dibuj_aula(screen, mesagrup, sillagrup)
            # estudiante.dibuj_estudiante(screen, estgrup)
            pygame.display.flip()
            # time.sleep(100000)


if __name__ == "__main__":
    v = View()
    v.main()
