from PyQt5.QtGui import QImage


class MovingEntity:
    mov_id: int
    max_mov_id: int
    pos_x: int
    pos_y: int
    img: QImage
    entity_pos_mapping: list

    def __init__(self, img, entity_pos_mapping):
        self.mov_id = 0
        self.max_mov_id = len(entity_pos_mapping)
        self.pos_x, self.pos_y = entity_pos_mapping[0]
        self.img = img
        self.entity_pos_mapping = entity_pos_mapping

    def update_position(self):
        self.mov_id += 1
        self.mov_id = self.mov_id % self.max_mov_id
        self.pos_x, self.pos_y = self.entity_pos_mapping[self.mov_id]
