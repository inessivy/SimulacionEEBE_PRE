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
class TitlePresenter:  # Presentar la ventana principal
    def __init__(self, rooms):  # Espacios que se manejaran
        self.rooms = rooms

    def on_combobox_changed(self, label):  # Acceder al espacio cuando es seleccionado
        qapp.switch_to_room(label)

    def on_guided_visit_button_clicked(self):  # Iniciar la visita guiada al clicar el boton
        qapp.start_guided_visit()

    def on_config_button_clicked(self):  # Iniciar la ventana configuración al clicar el botón
        qapp.switch_from_window_to_window('title_window', 'config_window')


class TitleWindow(QWidget):  # Configuración botones de la Pantalla principal
    def __init__(self, default_screen_size, rooms):
        super().__init__(parent=None)
        self.default_screen_size = default_screen_size
        self.rooms = rooms
        self.setWindowTitle("QMainWindow")
        self.setGeometry(*default_screen_size)
        self.presenter = TitlePresenter(rooms)
        self._create_title()
        self._create_rooms_combobox()
        self._create_guided_visit_button()
        self._create_config_button()

    def _create_title(self):  # Titulo de la pantalla principal
        title = QLabel(self)
        title.move(self.default_screen_size[2] // 10 + 30, self.default_screen_size[3] // 10)
        title.setText('<span style="font-size: 80px">Bienvenidos a la EEBE!</span>')
        title.adjustSize()

    def _create_rooms_combobox(self):  # Menu desplegable pantalla principal
        combo = QComboBox(self)
        for room in self.rooms.keys():
            combo.addItem(room)
        combo_geometry = [size // 5 for size in self.default_screen_size]
        combo_geometry[3] = self.default_screen_size[3] // 10
        combo.setGeometry(*combo_geometry)
        combo.move(self.default_screen_size[2] // 2 - combo_geometry[2] // 2, self.default_screen_size[3] // 2)
        font = combo.font()
        font.setPointSize(18)
        combo.setFont(font)
        combo.activated[str].connect(self.presenter.on_combobox_changed)

    def _create_guided_visit_button(self):  # Botón visita guiada
        button = QPushButton('Visita guiada', self)
        button_geometry = [size // 4 for size in self.default_screen_size]
        button_geometry[3] = self.default_screen_size[3] // 10
        button.setGeometry(*button_geometry)
        button.move(self.default_screen_size[2] // 2 - button_geometry[2] // 2, self.default_screen_size[3] // 3)
        font = button.font()
        font.setPointSize(18)
        button.setFont(font)
        button.clicked.connect(self.presenter.on_guided_visit_button_clicked)

    def _create_config_button(self):  # Botón configuración
        button = QPushButton('Configuración', self)
        button_geometry = [size // 4 for size in self.default_screen_size]
        button_geometry[3] = self.default_screen_size[3] // 10
        button.setGeometry(*button_geometry)
        button.move(self.default_screen_size[2] // 2 - button_geometry[2] // 2, self.default_screen_size[3] // 3 * 2)
        font = button.font()
        font.setPointSize(18)
        button.setFont(font)
        button.clicked.connect(self.presenter.on_config_button_clicked)