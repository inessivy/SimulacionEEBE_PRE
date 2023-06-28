import os
import random
import time
import pygame
import sys
from Aula import Aula
from Estudiante import Estudiante
from Profesor import  Profesor


class View():
    pygame.mixer.init()
    def __init__(self):
        self.size = (635, 730)
        # self.SONIDO_DIR = "sonidos proy"
        self.estudiantes = pygame.sprite.Group()
        self.place = Aula(70, 210, 5, 2)
        self.dest = pygame.sprite.Group()
        self.profesor = Profesor(self.place.entrada.rect.centerx, self.place.entrada.rect.centery, self.place)
        # self.sound_ruido = pygame.mixer.Sound(os.path.join(self.SONIDO_DIR, "sonido_aula.mp3"))
        # self.sound_bell = pygame.mixer.Sound(os.path.join(self.SONIDO_DIR, "campana.mp3"))
    def main(self):
        pygame.init()
        screen = pygame.display.set_mode(self.size)
        clock = pygame.time.Clock()

        # for i in range(random.randint(1, 40)):
        for i in range(40):
            estudiante = Estudiante(self.place.entrada.rect.centerx, self.place.entrada.rect.centery, self.place)
            self.estudiantes.add(estudiante)
            self.dest.add(estudiante.dest)

        while True:
            clock.tick(60)
            # self.sound_ruido.play()
            # self.sound0_ruido.set_volume(0.5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            current_time = pygame.time.get_ticks()  # return en que millisecond estoy

            # dibujar aula y estudiantes & update objetos
            screen.fill((0, 0, 0))
            self.place.dibuj_aula(screen)
                # (?) que entren varios est cada segundo
            self.estudiantes.draw(screen)
            # if 2000 < current_time:
            #     self.sound_bell.play()
            #     self.sound_bell.set_volume(0.8)

            if current_time > 5000:
                # self.sound_bell.stop()
                # self.sound_ruido.set_volume(0.2)
                screen.blit(self.profesor.image, (self.profesor.rect.centerx, self.profesor.rect.centery))
                self.profesor.update()

            # SALIR DEL AULA
            # if current_time > 60000:
            #     self.place.estudiantes_sentados.update()
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
            coll_s_dict = pygame.sprite.groupcollide(self.estudiantes,
                                                     pygame.sprite.Group(i.sillas for i in self.place.mesas), False, False)
            for i in coll_s_dict:
                if i.dest in coll_s_dict[i]:
                    i.sentado()

            coll_p_list = pygame.sprite.spritecollide(self.profesor, self.place.tarima.get_entradas(), False)
            if self.profesor.dest in coll_p_list:
                self.profesor.explicar()


            pygame.display.flip()

if __name__ == "__main__":
    v = View()
    v.main()
