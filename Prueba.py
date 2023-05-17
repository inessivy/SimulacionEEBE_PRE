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
    def escKeyPressEvent(self): #Para salir de la pagina y volver atras
        self.presenter.on_escape_pressed()

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
class Aula(RoomModel): #Pantalla del espacio Aula (se tiene que rellenar)
    def __init__(self):
        super().__init__()
        self.color = 255, 0, 0

class Cafeteria(RoomModel): #Rellenar
    def __init__(self):
        super().__init__()
        self.color = 0, 255, 0

class Pasillos(RoomModel): #Rellenar
    def __init__(self):
        super().__init__()
        self.color = 0, 0, 255

class Laboratorio(RoomModel):#Rellenar
    def __init__(self):
        super().__init__()
        self.color = 0, 0, 0


class Terraza(RoomModel): #Rellenar
    def __init__(self):
        super().__init__()
        self.color = 100, 100, 100

class VolverAtras(QObject): #Eventos que ocurren al pulsar teclas
    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Escape:
                obj.currentWidget().escKeyPressEvent()
        return super().eventFilter(obj, event)


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


default_screen_size = (400, 200, 1024, 512)

app = QApplication([]) #Interacciones de toda la aplicacion
qapp = MainWindow() #Interfaz (pantalla principal)
qapp.main()
qapp.show()
sys.exit(app.exec())
