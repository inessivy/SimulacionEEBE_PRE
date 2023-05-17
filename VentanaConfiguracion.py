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
class ConfigPresenter: #Acciones que recibe el Presenter para la ventana configuracion
    def __init__(self):
        self.sound_levels = {'Bajo': 3, 'Normal': 5, 'Alto': 7, 'Muy alto': 10}
        self.brightness_levels = ['25%', '50%', '75%', '100%']
        self.simulated_speed_levels = {'Lento': 0.5, 'Normal': 1, 'Rápido': 2, 'Muy Rápido': 4}
    def on_sound_checkbox_changed(self, state):
        qapp.is_volume_on = state == Qt.Checked
        qapp.change_volume()
    def on_sound_level_changed(self, label):
        qapp.volume = self.sound_levels[label]
        qapp.change_volume()
    def on_brightness_changed(self, label):
        qapp.brightness = int(label.replace('%', ''))
        print(qapp.brightness)
    def on_simulation_speed_changed(self, label):
        qapp.simulation_speed = self.simulated_speed_levels[label]
    def on_escape_pressed(self):
        qapp.switch_from_window_to_window('config_window', 'title_window')
class ConfigWindow(QWidget): #View ventana configuración
    def __init__(self, default_screen_size):
        super().__init__(parent=None)
        self.default_screen_size = default_screen_size
        self.setWindowTitle("ConfigWindow")
        self.setGeometry(*default_screen_size)
        self.presenter = ConfigPresenter()
        self._create_title()
        self._set_labels()
        self._create_sound_checkbox()
        self._create_sound_level_combobox()
        self._create_brightness_combobox()
        self._create_simulation_speed_level_combobox()
    def _create_title(self): #Titulo de la ventana
        title = QLabel(self)
        title.move(self.default_screen_size[2] // 10, self.default_screen_size[3] // 7)
        title.setText('<span style="font-size: 24px">CONFIGURACIÓN</span>')
        title.adjustSize()
    def _set_labels(self): #Opciones de configuración
        for idx, label in enumerate(['Sonido', 'Volumen', 'Brillo', 'Velocidad de simulación', 'Modo Oscuro']):
            self._set_label(label, idx + 2)
    def _set_label(self, label_text, index): #ns q es
        label = QLabel(self)
        label.move(self.default_screen_size[2] // 7, self.default_screen_size[3] // 7 * index)
        label.setText(f'<span style="font-size: 18px">{label_text}</span>')
        label.adjustSize()
    def _create_sound_checkbox(self): #Opcion para tickear sonido
        box = QCheckBox(self)
        box.move(self.default_screen_size[2] // 7 * 3, self.default_screen_size[3] // 7 * 2)
        box.setChecked(True)
        box.stateChanged.connect(self.presenter.on_sound_checkbox_changed)
    def _create_generic_combobox(self, labels, index, on_changed_method, default_comb_index=0): # Creacion de desplgable
        combo = QComboBox(self)
        for label in labels:
            combo.addItem(label)
        combo_geometry = [size // 12 for size in self.default_screen_size]
        combo_geometry[3] = self.default_screen_size[3] // 18
        combo.setGeometry(*combo_geometry)
        combo.move(self.default_screen_size[2] // 7 * 3 - combo_geometry[2] + 12,
                   self.default_screen_size[3] // 7 * index)
        combo.setCurrentIndex(default_comb_index)
        combo.activated[str].connect(on_changed_method)
    def _create_sound_level_combobox(self): #Seleccion del nivel de volumen
        self._create_generic_combobox(self.presenter.sound_levels, 3, self.presenter.on_sound_level_changed, 1)
    def _create_brightness_combobox(self): #seleccion nivel de brillo
        self._create_generic_combobox(self.presenter.brightness_levels, 4, self.presenter.on_brightness_changed, 3)
    def _create_simulation_speed_level_combobox(self): #Seleccion velocidad de simulacion
        self._create_generic_combobox(self.presenter.simulated_speed_levels, 5,
                                      self.presenter.on_simulation_speed_changed, 1)
    def escKeyPressEvent(self): #esto que es?
        self.presenter.on_escape_pressed()