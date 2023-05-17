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
#CONSTANTES
default_screen_size = (400, 200, 1024, 512)

# ----CLASES-----
# Diseño de Ventanas
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
#Interacciones entre todas las ventanas
from Interacciones import MainWindow
from VolverAtras import VolverAtras
app = QApplication([]) #Interacciones de toda la aplicacion
qapp = MainWindow() #Interfaz (pantalla principal)
qapp.main()
qapp.show()
sys.exit(app.exec())