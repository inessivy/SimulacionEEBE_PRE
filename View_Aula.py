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
        for k in range(2):
            for i in range(5):
                for j in range(4):
                    if j == 0:
                        des = (ox, oy)
                    else:
                        des = (DES[j - 1][0] + 50, oy)
                    DES.append(des)
                if k == 0:
                    oy += 100
                # else:
                # oy -= 100
            ox = 350
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

    def dibuj_mesa(self, pant, mx, my):  # mx = 70, my = 210
        mesa = self.load_image("mesa.jpg", self.IMG_DIR, alpha=False)
        pygame.draw.rect(pant, self.colores["BLACK"], (mx, my, 200, 45))
        # pant.blit(pygame.transform.scale(mesa, (198.75, 43.75)), (mx + 1.25, my + 1.25))
        msx = mx + 175
        mesasprite = Mesa(mx+1.25, my+1.25, mesa)
        pant.blit(pygame.transform.scale(mesasprite.image, (198.75, 43.75)), (mx+1.25, my+1.25))
        # sillas
        for i in range(1):
            self.dibuj_silla(pant, msx, my + 60)
            msx -= 50

    def dibuj_silla(self, pant, sx, sy):
        pygame.draw.rect(pant, self.colores["BLACK"], (sx, sy, 20, 20))

    def dibuj_suelo(self, pant, slx, sly):
        fondo = self.load_image("suelo2.png", self.IMG_DIR)
        for i in range(12):
            for j in range(12):
                pant.blit(pygame.transform.scale(fondo, (52, 60)), (5 + slx, 5 + sly))
                slx += 53
            sly += 61
            slx = 0

    def dibuj_puerta(self, pant):
        pygame.draw.rect(pant, self.colores["GBROWN"], (695, 50, 5, 100))

    def dibuj_tarima(self, pant, tx, ty):
        pygame.draw.rect(pant, self.colores["BLACK"], (5, 5, 540, 98))
        tarima = self.load_image("suelo azul.jpg", self.IMG_DIR, alpha=False)
        for i in range(2):
            for j in range(18):
                pant.blit(pygame.transform.scale(tarima, (30, 48)), (tx, ty))
                tx += 30
            tx = 3
            ty += 48

    def dibuj_mesa_prof(self, pant):
        pygame.draw.rect(pant, self.colores["BLACK"], (20, 50, 80, 45))
        pygame.draw.rect(pant, self.colores["GREY"], (21.25, 51.25, 78.75, 43.75,))

    def dibuj_aula(self, pant, tx, ty, mesx, mesy): #  tx=3, ty=5, mesx=70, mesy = 210
        self.dibuj_suelo(pant, 0, 0)
        self.dibuj_tarima(pant, 3, 5)
        self.dibuj_puerta(pant)
        self.dibuj_mesa_prof(pant)
        self.dibuj_mesa(pant, mesx, mesy)
        # for i in range(2):
            # for j in range(5):
                # if j == 0:
                    # self.dibuj_mesa(pant, mesx, mesy)
                # else:
                    # self.dibuj_mesa(pant, mesx, mesy)
                # mesy += 100
            # mesx += 280
            # mesy = 210

    def dibuj_estudiante(self, x, y, imagen): # x=600 y=80
        est = []
        # for i in range(random.randint(1, 40)):
        for i in range(3):
            DEST = self.destinos(65, 215)
            estd = Persona(x, y,
                          pygame.transform.scale(self.load_image(imagen, self.IMG_DIR, alpha=True), (60, 60)))
            estd.dir = random.choice(DEST)
            DEST.remove(estd.dir)
            estd.speedx = random.uniform(1, 3)
            estd.speedy = random.uniform(1, 3)
            est.append(estd)
        return est

    def main(self):
        import time
        pygame.init()
        # pantalla
        screen = pygame.display.set_mode(self.size)
        # crear objetos
        clock = pygame.time.Clock()


        while True:
            clock.tick(60)
            # actualizar objetos (diff acciones de objetos)
            est = self.dibuj_estudiante(600, 80, "estudiante.png")
            for i in est:
                i.update()
            # controles
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # actualizar pantalla
            screen.fill(self.colores["BLACK"])
            # DIBUJAR AULA
            self.dibuj_aula(screen, 3, 5, 70, 210)
            pygame.display.flip()
            # time.sleep(100000)
            for i in est:
                screen.blit(i.image, (i.rect.centerx, i.rect.centery))

            pygame.display.flip()


if __name__ == "__main__":
    v = View()
    v.main()
