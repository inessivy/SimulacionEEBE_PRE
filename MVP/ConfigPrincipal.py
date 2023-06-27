import os

import pygame
import yaml
from PyQt5.QtWidgets import QMainWindow, QStackedWidget

from MVP.Default import default_screen_size


class MainWindow(QMainWindow):

    """
    Es la ventana principal. Maneja los cambios entre widgets y contiene todos los parámetros necesarios para la
    aplicación
    """

    def __init__(self):
        from MVP.VIEW import RoomView, RoomHandlerView
        from MVP.MODEL import RoomHandlerPresenter, RoomHandlerModel
        from MVP.PRESENTER import RoomPresenter
        from main import KeyPressFilter
        super().__init__()

        self.setGeometry(*default_screen_size)
        pygame.init()
        pygame.mixer.music.load("C:/Users/soooo/Downloads/sonidopy.mp3")  # Hay que poner el path del mp3
        pygame.mixer.music.play(-1)

        self.is_volume_on = True
        self.volume = 5

        self.change_volume()

        room_config = self.read_room_config()

        self.brightness = 100
        self.simulation_speed = 1
        self.title_window = None
        self.config_window = None
        self.room_window = None

        self.view = QStackedWidget()
        self.setCentralWidget(self.view)

        self.rooms = room_config
        self.img_database = {key:  None  # QImage(os.path.join(project_path, 'path_foto.png'))
                             for key in self.rooms.keys()}
        # Se pueden añadir aquí las imágenes que quieres pegar en las habitaciones. Va con la estructura:
        # {nombre_habitacion: {tipo_imagen: imagen_cargada_con_QImage}}

        room_presenter = RoomPresenter()
        room_view = RoomView(room_presenter)
        room_presenter.start(room_view)

        room_handler_model = RoomHandlerModel(self.rooms)
        room_handler_presenter = RoomHandlerPresenter(room_handler_model, room_view, room_presenter,
                                                      img_database=self.img_database)
        self.room_handler_view = RoomHandlerView(room_handler_presenter)
        room_handler_presenter.view = self.room_handler_view
        self.current_room = None

        self.event_filter = KeyPressFilter()
        self.view.installEventFilter(self.event_filter)

    @staticmethod
    def read_room_config():
        project_path = os.getcwd()
        with open(os.path.join(project_path, 'TodoCafeteria', 'Configuracion.yaml'), "r", encoding='utf-8') as file:
            obj = yaml.safe_load(file)
        return obj

    def change_volume(self):
        if self.is_volume_on:
            pygame.mixer.music.set_volume(self.volume / 10)
        else:
            pygame.mixer.music.set_volume(0)

    def main(self):
        from MVP.VIEW import ConfigWindow, TitleWindow
        self.title_window = TitleWindow(default_screen_size, self.rooms)
        self.config_window = ConfigWindow(default_screen_size)
        self.room_window = None
        self.view.addWidget(self.title_window)

    def switch_from_window_to_window(self, from_window_name, to_window_name):
        """
        Cambia de una ventana a otra de la app
        """
        from_window = getattr(self, from_window_name)
        self.view.removeWidget(from_window)
        to_window = getattr(self, to_window_name)
        self.view.addWidget(to_window)
        self.view.setCurrentWidget(to_window)

    def switch_to_room(self, room_name):
        """
        Cambia a una habitación desde el main menu
        """
        self.view.removeWidget(self.title_window)
        self.room_window = self.room_handler_view.change_room(room_name)
        self.view.addWidget(self.room_window)
        self.view.setCurrentWidget(self.room_window)

    def start_guided_visit(self):
        """
        Al clicar desde el main menu, empieza una visita guiada.
        """
        self.room_handler_view.start_guided()
        self.view.removeWidget(self.title_window)
        self.room_window = self.room_handler_view.change_room(list(self.rooms.keys())[0])
        self.view.addWidget(self.room_window)
        self.view.setCurrentWidget(self.room_window)
