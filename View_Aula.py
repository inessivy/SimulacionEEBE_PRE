import os
import random
import pygame
import sys
from TodoAula.Aula import Aula
from TodoAula.Estudiante import Estudiante
from Profesor import Profesor

class View():
    pygame.mixer.init()
    def __init__(self):
        self.size = (635, 730)
        self.SONIDO_DIR = "sonidos proy"
        self.place = Aula(70, 210, 5, 2)
        self.estudiantes = pygame.sprite.Group()
        self.estudiantes_sentados = pygame.sprite.Group()
        self.pasillos = self.place.get_ent_pasillos()
        self.entradas_mesas = self.place.ent_mesas
        self.sillas = self.place.sillas
        self.dest = pygame.sprite.Group()
        self.profesor = Profesor(590, 75, self.place)
        self.sound_bell = pygame.mixer.Sound(os.path.join(self.SONIDO_DIR, "campana.wav"))
        self.entradas = pygame.sprite.Group()
        self.entradas.add(self.place.tarima.get_entradas().sprites())
        self.entradas.add(self.place.entrada)

    def cambio_grupo(self, estudiante):
        if estudiante.rect.center == estudiante.dir:
            self.estudiantes.remove(estudiante)
            self.estudiantes_sentados.add(estudiante)

    def main(self):
        pygame.init()
        screen = pygame.display.set_mode(self.size)
        clock = pygame.time.Clock()
        pygame.mixer.music.load(os.path.join(self.SONIDO_DIR, "sonido_aula.wav"))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)
        finish_time = 100000

        for i in range(random.randint(1, 40)):
            estudiante = Estudiante(self.place.entrada.rect.centerx, self.place.entrada.rect.centery, self.place)
            self.estudiantes.add(estudiante)
            self.dest.add(estudiante.dest)

        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            current_time = pygame.time.get_ticks()

            screen.fill((0, 0, 0))
            self.place.dibuj_aula(screen)
            self.estudiantes.draw(screen)
            self.estudiantes_sentados.draw(screen)

            if current_time > 30000:
                if current_time < 33000:
                    self.sound_bell.play(0, 3000, 1000)
                    self.sound_bell.set_volume(0.8)
                    pygame.mixer.music.set_volume(0.1)
                screen.blit(self.profesor.image,
                            (self.profesor.rect.centerx, self.profesor.rect.centery))
                self.profesor.update()
            self.estudiantes.update()
            self.estudiantes_sentados.update()

            coll_dict = pygame.sprite.groupcollide(self.estudiantes, self.dest, False, False)
            for i in coll_dict:
                if i.dest in coll_dict[i]:
                    i.go_mesa(i.dest)
            coll_m_dict = pygame.sprite.groupcollide(self.estudiantes, self.place.ent_mesas, False, False)
            for i in coll_m_dict:
                if i.dest in coll_m_dict[i]:
                    i.go_silla(i.dest)
            coll_s_dict = pygame.sprite.groupcollide(self.estudiantes,self.sillas, False, False)
            for i in coll_s_dict:
                if i.dest in coll_s_dict[i]:
                    i.sentado()
                self.cambio_grupo(i)
            coll_p_list = pygame.sprite.spritecollide(self.profesor, self.entradas, False)
            if self.profesor.dest in coll_p_list:
                self.profesor.explicar()
            if self.place.entrada in coll_p_list:
                pygame.quit()

            if current_time - finish_time > 0:
                if current_time - finish_time < 3000:
                    self.sound_bell.play(0, 3000, 1000)
                self.profesor.salir()

            pygame.display.flip()

if __name__ == "__main__":
    v = View()
    v.main()
