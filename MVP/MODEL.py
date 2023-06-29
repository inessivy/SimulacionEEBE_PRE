import os
import random
from abc import ABC

import pygame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QTransform

from Profesor import Profesor
from TodoCafeteria.Cafeteria import Entity
from TodoCafeteria.MovimientosCafe import MovingEntity

from MVP.Default import default_screen_size

from pygame import KEYDOWN, K_ESCAPE
import sys
from TodoAula.Aula import Aula
from TodoAula.Estudiante import Estudiante


class RoomHandlerModel:
    def __init__(self, room_config):
        self.rooms = room_config
        self.current_room = None
        self.current_room_name = None


class RoomModel(ABC):
    img_path = os.path.join(os.getcwd(), 'imagenesproy')

    def __init__(self, room_name, room_info):
        self.room_name = room_name
        self.entities = self.get_entities(room_info)
        if room_name == 'Aula':
            self.model = AulaModel()
            self.model.start()
            self.model.main()

    def get_entities(self, room_info):

        if self.room_name == 'Aula':
            return None

        entities = []
        for entity_type, entity_info in room_info.items():
            entity_img = QPixmap(os.path.join(self.img_path, entity_info['img_name']))
            if 'img_size' in entity_info:
                entity_img = entity_img.scaled(*entity_info['img_size'])

            if 'img_rotation' in entity_info:
                transform = QTransform().rotate(entity_info['img_rotation'])
                entity_img = entity_img.transformed(transform, Qt.SmoothTransformation)

            if entity_type == 'bg':
                entity_img = entity_img.scaled(*default_screen_size[2:])
                entities.append(Entity(entity_img, [0, 0]))
            elif entity_type.startswith('entity'):
                entities.append(Entity(entity_img, entity_info['position']))
            elif entity_type.startswith('moving_entity'):
                entities.append(MovingEntity(entity_img, entity_info['entity_pos_mapping']))
            else:
                print(f'Entity type must be bg, entity or moving_entity. {entity_type} not valid.')
        return entities

    def update_position(self):
        if self.room_name == 'Aula':
            self.model.main()
        else:
            for entity in self.entities:
                entity.update_position()


class AulaModel:
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

    def start(self):
        # pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        pygame.mixer.music.load(os.path.join(self.SONIDO_DIR, "sonido_aula.wav"))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)
        # finish_time = 100000

        for i in range(random.randint(1, 40)):
            estudiante = Estudiante(self.place.entrada.rect.centerx, self.place.entrada.rect.centery, self.place)
            self.estudiantes.add(estudiante)
            self.dest.add(estudiante.dest)

        # while True:
    def main(self):
        self.clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current_time = pygame.time.get_ticks()

        self.screen.fill((0, 0, 0))
        self.place.dibuj_aula(self.screen)
        self.estudiantes.draw(self.screen)
        self.estudiantes_sentados.draw(self.screen)

        if current_time > 30000:
            if current_time < 33000:
                self.sound_bell.play(0, 3000, 1000)
                self.sound_bell.set_volume(0.8)
                pygame.mixer.music.set_volume(0.1)
            self.screen.blit(self.profesor.image, (self.profesor.rect.centerx, self.profesor.rect.centery))
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
        coll_s_dict = pygame.sprite.groupcollide(self.estudiantes, self.sillas, False, False)
        for i in coll_s_dict:
            if i.dest in coll_s_dict[i]:
                i.sentado()
            self.cambio_grupo(i)
        coll_p_list = pygame.sprite.spritecollide(self.profesor, self.entradas, False)
        if self.profesor.dest in coll_p_list:
            self.profesor.explicar()
        if self.place.entrada in coll_p_list:
            pygame.quit()

        if current_time - 100000 > 0:
            if current_time - 100000 < 3000:
                self.sound_bell.play(0, 3000, 1000)
            self.profesor.salir()
