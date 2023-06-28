from PyQt5.QtCore import Qt

from MVP.MODEL import RoomModel


class TitlePresenter:
    def __init__(self, rooms):
        self.rooms = rooms

    def on_combobox_changed(self, label):
        from main import qapp
        qapp.switch_to_room(label)

    def on_guided_visit_button_clicked(self):
        from main import qapp
        qapp.start_guided_visit()

    def on_config_button_clicked(self):
        from main import qapp
        qapp.switch_from_window_to_window('title_window', 'config_window')


class ConfigPresenter:
    def __init__(self):
        self.sound_levels = {'Bajo': 3, 'Normal': 5, 'Alto': 7, 'Muy alto': 10}
        self.brightness_levels = ['25%', '50%', '75%', '100%']
        self.simulated_speed_levels = {'Lento': 0.5, 'Normal': 1, 'Rápido': 4, 'Muy Rápido': 10}

    def on_sound_checkbox_changed(self, state):
        from main import qapp
        qapp.is_volume_on = state == Qt.Checked
        qapp.change_volume()

    def on_sound_level_changed(self, label):
        from main import qapp
        qapp.volume = self.sound_levels[label]
        qapp.change_volume()

    def on_brightness_changed(self, label):
        from main import qapp
        qapp.brightness = int(label.replace('%', ''))
        print(qapp.brightness)

    def on_simulation_speed_changed(self, label):
        from main import qapp
        qapp.simulation_speed = self.simulated_speed_levels[label]

    def on_escape_pressed(self):
        from main import qapp
        qapp.switch_from_window_to_window('config_window', 'title_window')

class RoomHandlerPresenter:
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
        from main import qapp
        rooms_list = list(self.room_model.rooms.keys())
        next_room_idx = (rooms_list.index(self.room_model.current_room_name) + 1) % len(rooms_list)
        next_room_name = rooms_list[next_room_idx]
        qapp.switch_to_room(next_room_name)

    def start_guided(self):
        from main import qapp
        self.view.guided_timer.start(50000 // qapp.simulation_speed)

    def change_room(self, room_name):
        self.room_model.current_room = RoomModel(room_name, self.room_model.rooms[room_name])
        self.room_model.current_room_name = room_name
        self.room_view.img_database = self.img_database[room_name]
        self.room_presenter.model = self.room_model.current_room
        return self.room_view


class RoomPresenter:
    def __init__(self):
        self.model = None
        self.view = None

    def start(self, view):
        self.view = view

    def get_room_entities(self):
        return self.model.entities

    def handle_escape_key_press(self):
        from main import qapp
        qapp.room_handler_view.guided_timer.stop()
        qapp.switch_from_window_to_window('room_window', 'title_window')

    def update_model(self):
        self.model.update_position()
        self.view.update_view()


