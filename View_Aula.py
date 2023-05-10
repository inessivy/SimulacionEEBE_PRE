import random
import pygame, sys, os
from Persona import Persona
from Mesa import Mesa


class View():
    def __init__(self):
        self.size = (650, 742)
        self.IMG_DIR = "imagenesproy"
        self.SONIDO_DIR = "sonidos proy"
        self.colores = {
            "BLUE": [96, 130, 182],
            "BLACK": [0, 0, 0],
            "GBROWN": [150, 105, 25],
            "WHEAT": [245, 222, 179],
            "GREY": [240, 240, 240],
        }

    def destinos(self, ox, oy):
        DES = []
        for i in range(5):
            for j in range(4):
                if j == 0:
                    des = (ox, oy)
                else:
                    des = (DES[j - 1][0] + 50, oy)
                DES.append(des)
            oy += 100
        for i in range(5):
            for j in range(4):
                if j == 0:
                    des = (350, oy - 500)
                else:
                    des = (DES[-1][0] + 50, oy - 500)
                DES.append(des)
            oy += 100
        return DES

    # Para poner objetos. deben estar en IMG_DIR
    def load_image(self, nombre, dir_imagen, alpha=False):
        ruta = os.path.join(dir_imagen, nombre)
        try:
            image = pygame.image.load(ruta)
        except:
            print("No se puede cargar imagen: " + ruta)
            sys.exit(1)
        if alpha is True:
            image = image.convert_alpha()
        else:
            image = image.convert()
        return image

    def dibuj_estudiante(self, x, y, imagen): # x=600 y=80
        est = []
        # for i in range(random.randint(1, 40)):
        for i in range(1):
            # DEST = self.destinos(65, 250)
            dest = (215, 250)
            estd = Persona(x, y,
                          pygame.transform.scale(self.load_image(imagen, self.IMG_DIR, alpha=True), (60, 60)))
            # estd.dir = random.choice(DEST)
            estd.dir = dest
            # DEST.remove(estd.dir)
            estd.speedx = random.uniform(1, 3)
            estd.speedy = random.uniform(1, 3)
            est.append(estd)
        # print(DEST)
        return est


    def colision(self, estudiante, mesa_silla):
        estudiante.speedx *= -1
        estudiante.speedy *= -1

    def main(self):
        import time
        pygame.init()
        # pantalla
        screen = pygame.display.set_mode(self.size)
        # crear objetos
        clock = pygame.time.Clock()
        # screen.fill(self.colores["BLACK"])
        est = self.dibuj_estudiante(600, 80, "estudiante.png")

        while True:
            clock.tick(60)
            # DIBUJAR AULA
            self.dibuj_aula(screen, 3, 5, 70, 210)
            una_mesa = self.dibuj_mesa(screen, 70, 210)
            # actualizar objetos (diff acciones de objetos)
            m = pygame.sprite.Group()
            m.add(una_mesa)
            for i in est:
                # g = pygame.sprite.Group()
                # g.add(est)
                # colisiones = pygame.sprite.groupcollide(g, m, False, False)
                i.update()
                screen.blit(i.image, (i.rect.centerx, i.rect.centery))
            # controles
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # print(colisiones)
            # actualizar pantalla
            pygame.display.flip()
            # time.sleep(100000)


if __name__ == "__main__":
    v = View()
    v.main()
