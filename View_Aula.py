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
        self.dest = pygame.sprite.Group()


    def main(self):
        pygame.init()
        screen = pygame.display.set_mode(self.size)
        clock = pygame.time.Clock()

        # for i in range(random.randint(1, 40)):
        for i in range(20):
            estudiante = Estudiante(600, 80, self.place)
            self.estudiantes.add(estudiante)
            self.dest.add(estudiante.dest)
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
            self.estudiantes.update()
            # detectar colisiones
            coll_dict = pygame.sprite.groupcollide(self.estudiantes, self.dest, False, False)
            for i in coll_dict:
                if i.dest in coll_dict[i]:
                    i.go_mesa(i.dest)
            coll_m_dict = pygame.sprite.groupcollide(self.estudiantes, self.place.ent_mesas, False, False)
            for i in coll_m_dict:
                if i.dest in coll_m_dict[i]:
                    i.go_silla(i.dest)
            #     self.estudiantes.remove(i)
            #     self.place.estudiantes_sentados.add(i)
            # self.place.estudiantes_sentados.draw(screen)

            pygame.display.flip()


if __name__ == "__main__":
    v = View()
    v.main()
