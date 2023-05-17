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

class VolverAtras(QObject): #Eventos que ocurren al pulsar teclas
    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Escape:
                obj.currentWidget().escKeyPressEvent()
        return super().eventFilter(obj, event)