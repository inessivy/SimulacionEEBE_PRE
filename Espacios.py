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
class RoomModel: #Mismo modelo para todos los espacios
    def __init__(self):
        self.x = 0
        self.y = 0
        self.radius = 50
        self.delta = 5
        self.color = 255, 0, 0
    def update_position(self):
        self.x += self.delta
        self.y += self.delta
        if self.x + self.radius >= 100 or self.x - self.radius <= 0:
            self.delta *= -1
        if self.y + self.radius >= 100 or self.y - self.radius <= 0:
            self.delta *= -1
class RoomPresenter: #Logica de los espacios
    def __init__(self):
        self.model = None
        self.view = None
    def start(self, view):
        self.view = view
    def get_color(self):
        return self.model.color
    def get_circle_rect(self):
        return (self.model.x - self.model.radius, self.model.y - self.model.radius,
                self.model.radius * 2, self.model.radius * 2)
    def handle_escape_key_press(self): #vuelta a la ventana principal
        qapp.room_handler_view.guided_timer.stop()
        qapp.switch_from_window_to_window('room_window', 'title_window')
    def update_model(self):
        self.model.update_position()
        self.view.update_view()
class RoomView(QWidget): #Visualizar el espacio
    def __init__(self, presenter):
        super().__init__()
        self.img_database = None
        self.presenter = presenter
        self.setGeometry(*default_screen_size)
        self.setWindowTitle("Moving Circle")
    def paintEvent(self, event):
        painter = QPainter(self)
        if self.img_database is not None:
            painter.drawImage(0, 0, self.img_database['bg'].scaled(*default_screen_size[2:]))
        painter.setBrush(QColor(*self.presenter.get_color()))
        painter.drawEllipse(*self.presenter.get_circle_rect())
    def escKeyPressEvent(self): #Volver a la pantalla principal con Esc
        self.presenter.handle_escape_key_press()
    def update_view(self):
        self.update()