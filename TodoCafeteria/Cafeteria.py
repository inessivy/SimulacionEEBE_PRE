from PyQt5.QtGui import QImage


class Entity:
    pos_x: int
    pos_y: int
    img: QImage

    def __init__(self, img, position):
        self.img = img
        self.pos_x, self.pos_y = position

    def update_position(self):
        pass
