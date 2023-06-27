import os
from abc import ABC

import pygame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QTransform

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


class RoomHandlerPresenter:
    def __init__(self, room_model, room_view, room_presenter, img_database):
        self.room_model = room_model
        self.view = None
        self.room_view = room_view
        self.img_database = img_database
        self.room_presenter = room_presenter

    def main(self):
        if self.room_presenter.model:
            self.room_presenter.update_model()

    def main_guided(self):
        from main import qapp
        rooms_list = list(self.room_model.rooms.keys())
        next_room_idx = (rooms_list.index(self.room_model.current_room_name) + 1) % len(rooms_list)
        next_room_name = rooms_list[next_room_idx]
        qapp.switch_to_room(next_room_name)

    def start_guided(self):
        from main import qapp
        self.view.guided_timer.start(50000 // qapp.simulation_speed)

    def change_room(self, room_name):
        self.room_model.current_room = RoomModel(room_name, self.room_model.rooms[room_name])
        self.room_model.current_room_name = room_name
        self.room_view.img_database = self.img_database[room_name]
        self.room_presenter.model = self.room_model.current_room
        return self.room_view


class RoomModel(ABC):
    img_path = os.path.join(os.getcwd(), 'imagenesproy')

    def __init__(self, room_name, room_info):
        self.room_name = room_name
        self.entities = self.get_entities(room_info)
        if room_name == 'Aula':
            self.model = AulaModel()
            self.model.start()

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
        self.size = default_screen_size[2:]
        self.SONIDO_DIR = "sonidos proy"
        self.estudiantes = pygame.sprite.Group()
        self.sillas = pygame.sprite.Group()
        self.place = Aula(70, 210, 5, 2)
        self.dest = pygame.sprite.Group()
        self.screen = None
        self.clock = None

    def start(self):
        pygame.init()
        self.screen = pygame.Surface(self.size)
        self.clock = pygame.time.Clock()

        # for i in range(random.randint(1, 40)):
        for i in range(10):
            estudiante = Estudiante(600, 80, self.place)
            self.estudiantes.add(estudiante)
            self.dest.add(estudiante.dest)
        for m in self.place.mesas:
            for s in m.sillas:
                self.sillas.add(s)

    def main(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
        # scollision_dict = pygame.sprite.groupcollide(self.estudiantes, self.sillas, False, False)
        # print(scollision_dict)

        # dibujar aula y estudiantes
        self.place.dibuj_aula(self.screen)
        self.estudiantes.draw(self.screen)
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
