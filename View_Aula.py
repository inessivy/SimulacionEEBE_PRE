import random
import pygame
import sys
from Aula import Aula
from Estudiante import Estudiante


class View():
    def __init__(self):
        self.size = (650, 742)
        self.SONIDO_DIR = "sonidos proy"
        self.estudiantes = pygame.sprite.Group()
        self.sillas = pygame.sprite.Group()
        self.place = Aula(70, 210, 5, 2)

    def main(self):
        pygame.init()
        screen = pygame.display.set_mode(self.size)
        clock = pygame.time.Clock()

        # for i in range(random.randint(1, 40)):
        for i in range(1):
            estudiante = Estudiante(600, 80, self.place)
            estudiante.dir = random.choice(estudiante.dest)
            self.estudiantes.add(estudiante)
        for m in self.place.mesas:
            for s in m.sillas:
                self.sillas.add(s)

        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # scollision_dict = pygame.sprite.groupcollide(self.estudiantes, self.sillas, False, False)
            # print(scollision_dict)

            # dibujar aula y estudiantes
            self.place.dibuj_aula(screen)
            self.estudiantes.draw(screen)
            # update objetos
            for i in self.estudiantes:
                i.update()
                i.cambio_destino()

            pygame.display.flip()
            # time.sleep(100000)


if __name__ == "__main__":
    v = View()
    v.main()
