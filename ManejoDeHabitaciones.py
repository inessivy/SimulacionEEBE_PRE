import os
import sys

import pygame
from PyQt5.QtCore import Qt, QTimer, QEvent, QObject
from PyQt5.QtGui import QImage, QPainter, QColor

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QComboBox,
    QPushButton,
    QCheckBox, QWidget, QStackedWidget,
)

class RoomHandlerModel: #Model para el manejo de habitaciones
    def __init__(self, rooms):
        self.rooms = rooms
        self.current_room = None
        self.current_room_name = None
class RoomHandlerPresenter:  #Logica del manejo de habitaciones
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
        rooms_list = list(self.room_model.rooms.keys())
        next_room_idx = (rooms_list.index(self.room_model.current_room_name) + 1) % len(rooms_list)
        next_room_name = rooms_list[next_room_idx]
        qapp.switch_to_room(next_room_name)
    def start_guided(self):
        self.view.guided_timer.start(2000 // qapp.simulation_speed)
    def change_room(self, room_name): #Cambiar de espacio en la visita guiada
        self.room_model.current_room = self.room_model.rooms[room_name]()
        self.room_model.current_room_name = room_name
        self.room_view.img_database = self.img_database[room_name]
        self.room_presenter.model = self.room_model.current_room
        return self.room_view
class RoomHandlerView: #Visualizacion de cambios entre espacios
    def __init__(self, presenter):
        self.presenter = presenter
        self.timer = QTimer()
        self.timer.timeout.connect(self.presenter.main)
        self.guided_timer = QTimer()
        self.guided_timer.timeout.connect(self.presenter.main_guided)
    def start_guided(self):
        self.presenter.start_guided()
    def change_room(self, room_name):
        self.timer.start(50 // qapp.simulation_speed)
        return self.presenter.change_room(room_name)