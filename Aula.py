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

from Espacios import RoomModel, RoomView, RoomPresenter

class Aula(RoomModel): #Pantalla del espacio Aula (se tiene que rellenar)
    def __init__(self):
        super().__init__()
        self.color = 255, 0, 0