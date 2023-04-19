import random, pygame.sprite, View_Aula

IMG_DIR = "imagenesproy"
SONIDO_DIR = "sonidos proy"

class Estudiante(pygame.sprite.Sprite):
    def __init__(self, posicion):
        pygame.sprite.Sprite.__init__(self)
        self.posx = posicion[0]
        self.posy = posicion[1]
        self.image = load_image("estudiante.jpg", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.speed = [3, 3]

    def direccion(self):
        self.dirx = random.randrange(650)
        self.diry = random.randrange(742)
        return self.dirx, self.diry

    def mover(self):
        self.posx += self.speed[0]
        self.posy += self.speed[1]
        self.rect.move_ip


    def parar(self):
        pass
