from time import sleep
import numpy as np

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QComboBox, QCheckBox, QLabel, QPushButton


from MVP.Default import default_screen_size
from MVP.PRESENTER import TitlePresenter, ConfigPresenter

import pygame


class TitleWindow(QWidget):
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

    def _create_title(self):
        """
        Genera el título
        """
        title = QLabel(self)
        title.move(self.default_screen_size[2] // 10 + 30, self.default_screen_size[3] // 10)
        title.setText('<span style="font-size: 80px">Bienvenidos a la EEBE!</span>')
        title.adjustSize()

    def _create_rooms_combobox(self):
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

    def _create_guided_visit_button(self):
        button = QPushButton('Visita guiada', self)
        button_geometry = [size // 4 for size in self.default_screen_size]
        button_geometry[3] = self.default_screen_size[3] // 10
        button.setGeometry(*button_geometry)
        button.move(self.default_screen_size[2] // 2 - button_geometry[2] // 2, self.default_screen_size[3] // 3)
        font = button.font()
        font.setPointSize(18)
        button.setFont(font)
        button.clicked.connect(self.presenter.on_guided_visit_button_clicked)

    def _create_config_button(self):
        button = QPushButton('Configuración', self)
        button_geometry = [size // 4 for size in self.default_screen_size]
        button_geometry[3] = self.default_screen_size[3] // 10
        button.setGeometry(*button_geometry)
        button.move(self.default_screen_size[2] // 2 - button_geometry[2] // 2, self.default_screen_size[3] // 3 * 2)
        font = button.font()
        font.setPointSize(18)
        button.setFont(font)
        button.clicked.connect(self.presenter.on_config_button_clicked)


class ConfigWindow(QWidget):
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

    def _create_title(self):
        title = QLabel(self)
        title.move(self.default_screen_size[2] // 10, self.default_screen_size[3] // 7)
        title.setText('<span style="font-size: 24px">CONFIGURACIÓN</span>')
        title.adjustSize()

    def _set_labels(self):
        for idx, label in enumerate(['Sonido', 'Volumen', 'Brillo', 'Velocidad de simulación', 'Modo Oscuro']):
            self._set_label(label, idx + 2)

    def _set_label(self, label_text, index):
        label = QLabel(self)
        label.move(self.default_screen_size[2] // 7, self.default_screen_size[3] // 7 * index)
        label.setText(f'<span style="font-size: 18px">{label_text}</span>')
        label.adjustSize()

    def _create_sound_checkbox(self):
        box = QCheckBox(self)
        box.move(self.default_screen_size[2] // 7 * 3, self.default_screen_size[3] // 7 * 2)
        box.setChecked(True)
        box.stateChanged.connect(self.presenter.on_sound_checkbox_changed)

    def _create_generic_combobox(self, labels, index, on_changed_method, default_comb_index=0):
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

    def _create_sound_level_combobox(self):
        self._create_generic_combobox(self.presenter.sound_levels, 3, self.presenter.on_sound_level_changed, 1)

    def _create_brightness_combobox(self):
        self._create_generic_combobox(self.presenter.brightness_levels, 4, self.presenter.on_brightness_changed, 3)

    def _create_simulation_speed_level_combobox(self):
        self._create_generic_combobox(self.presenter.simulated_speed_levels, 5,
                                      self.presenter.on_simulation_speed_changed, 1)

    def escKeyPressEvent(self):
        self.presenter.on_escape_pressed()


class RoomHandlerView:
    def __init__(self, presenter):
        self.presenter = presenter

        self.timer = QTimer()
        self.timer.timeout.connect(self.presenter.main)

        self.guided_timer = QTimer()
        self.guided_timer.timeout.connect(self.presenter.main_guided)

    def start_guided(self):
        self.presenter.start_guided()

    def change_room(self, room_name):
        from main import qapp
        self.timer.start(150 // qapp.simulation_speed)
        return self.presenter.change_room(room_name)


class RoomView(QWidget):
    def __init__(self, presenter):
        super().__init__()

        self.img_database = None
        self.presenter = presenter
        self.setGeometry(*default_screen_size)

        self.setWindowTitle("Moving Circle")

    def paintEvent(self, event):
        if self.presenter.model.room_name == 'Aula':
            image = pygame.surfarray.array3d(self.presenter.model.model.screen)
            image = np.swapaxes(image, 0, 1)  # Swap width and height
            image = np.ascontiguousarray(image)  # Convert to a contiguous C-style array

            height, width, channels = image.shape
            bytes_per_line = channels * width

            image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)
            # image = image.rgbSwapped()

            painter = QPainter(self)
            painter.drawImage(0, 0, image)
        else:
            from main import qapp
            painter = QPainter(self)


            entities = self.presenter.get_room_entities()
            for entity in entities:
                painter.drawPixmap(entity.pos_x, entity.pos_y, entity.img)

            sleep(0.5 / qapp.simulation_speed)

    def escKeyPressEvent(self):
        self.presenter.handle_escape_key_press()

    def update_view(self):
        self.update()
