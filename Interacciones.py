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
default_screen_size = (400, 200, 1024, 512)

from VentanaPrincipal import TitlePresenter, TitleWindow
from VentanaConfiguracion import ConfigPresenter,ConfigWindow
# Manejo de Espacios
from ManejoDeHabitaciones import RoomHandlerModel, RoomHandlerPresenter, RoomHandlerView
#Espacios
from Espacios import RoomModel, RoomView, RoomPresenter
from Aula import Aula
from Cafeteria import Cafeteria
from Pasillos import Pasillos
from Laboratorio import Laboratorio
from Terraza import Terraza

from VolverAtras import VolverAtras

class MainWindow(QMainWindow): #Interacciones de la ventana principal
    def __init__(self):
        super().__init__()
        self.setGeometry(*default_screen_size)
        project_path = os.getcwd()
        pygame.init()
        pygame.mixer.music.load("C:/Users/soooo/Downloads/sonidopy.mp3")  # Hay que poner el path del mp3
        pygame.mixer.music.play(-1)
        self.is_volume_on = True
        self.volume = 5
        self.change_volume()
        self.rooms = {'aula': Aula, 'cafetería': Cafeteria, 'pasillos': Pasillos,
                      'laboratorio': Laboratorio, 'terraza': Terraza}
        self.brightness = 100
        self.simulation_speed = 1
        self.title_window = None
        self.config_window = None
        self.room_window = None
        self.view = QStackedWidget()
        self.setCentralWidget(self.view)
        self.img_database = {key:  None  # QImage(os.path.join(project_path, 'path_foto.png'))
                             for key in self.rooms.keys()}
        room_presenter = RoomPresenter()
        room_view = RoomView(room_presenter)
        room_presenter.start(room_view)
        room_handler_model = RoomHandlerModel(self.rooms)
        room_handler_presenter = RoomHandlerPresenter(room_handler_model, room_view, room_presenter,
                                                      img_database=self.img_database)
        self.room_handler_view = RoomHandlerView(room_handler_presenter)
        room_handler_presenter.view = self.room_handler_view
        self.current_room = None
        self.event_filter = VolverAtras()
        self.view.installEventFilter(self.event_filter)
    def change_volume(self):
        print(self.volume)
        if self.is_volume_on:
            pygame.mixer.music.set_volume(self.volume / 10)
        else:
            pygame.mixer.music.set_volume(0)
    def main(self): #Juntar todas las ventanas en la app
        self.title_window = TitleWindow(default_screen_size, self.rooms)
        self.config_window = ConfigWindow(default_screen_size)
        self.room_window = None
        self.view.addWidget(self.title_window)
    def switch_from_window_to_window(self, from_window_name, to_window_name): #cambio de ventana
        from_window = getattr(self, from_window_name)
        self.view.removeWidget(from_window)
        to_window = getattr(self, to_window_name)
        self.view.addWidget(to_window)
        self.view.setCurrentWidget(to_window)
    def switch_to_room(self, room_name): #De la pantalla principal al espacio escogido
        self.view.removeWidget(self.title_window)
        self.room_window = self.room_handler_view.change_room(room_name)
        self.view.addWidget(self.room_window)
        self.view.setCurrentWidget(self.room_window)
    def start_guided_visit(self): #Iniciar la visita guiada al clicar el boton del main menu
        self.room_handler_view.start_guided()
        self.view.removeWidget(self.title_window)
        self.room_window = self.room_handler_view.change_room('aula')
        self.view.addWidget(self.room_window)
        self.view.setCurrentWidget(self.room_window)