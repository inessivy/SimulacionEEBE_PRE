import random

import pygame, sys, os
from Estudiante import Estudiante

size = (650, 742)
IMG_DIR = "imagenesproy"
SONIDO_DIR = "sonidos proy"

#colores
BLUE = [96, 130, 182]
BLACK = [0, 0, 0]
GBROWN = [150, 105, 25]
WHEAT = [245, 222, 179]
DESKPROF = [193, 154, 107]


# Para poner objetos. deben estar en IMG_DIR
def load_image(nombre, dir_imagen, alpha=False):
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


def main():
    pygame.init()
    pygame.mixer.init()
    #pantalla
    screen = pygame.display.set_mode(size)
    fondo = load_image("suelo.jpg", IMG_DIR)
    #sonidos
    #crear objetos
    clock = pygame.time.Clock()
    est = []
    for i in range(random.randrange(60)):
        est.append(Estudiante(600, 80, pygame.transform.scale(load_image("estudiante.png", IMG_DIR, alpha=True), (60, 60))))
    while True:
        clock.tick(60)
        # actualizar objetos (diff acciones de objetos)
        for i in est:
            i.update()
        #controles
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #actualizar pantalla
        screen.fill(BLACK)
        #dibujar pantalla
        w = 0
        h = 0
        for i in range(12):
            for j in range(12):
                screen.blit(pygame.transform.scale(fondo, (52, 60)), (5+w, 5+h))
                w += 53
            h += 61
            w = 0
        pygame.draw.rect(screen, GBROWN, (695, 50, 5, 100))
        pygame.draw.rect(screen, BLACK, (5, 5, 550, 100))
        pygame.draw.rect(screen, BLUE, (6.25, 6.25, 547.5, 97.5))
        pygame.draw.rect(screen, BLACK, (20, 50, 80, 45))
        pygame.draw.rect(screen, DESKPROF, (21.25, 51.25, 78.75, 43.75,))
        pygame.draw.rect(screen, BLACK, (70, 190, 200, 40))
        pygame.draw.rect(screen, WHEAT, (71.25, 191.25, 198.75, 38.75))
        # dibujar objetos
        for i in est:
            screen.blit(i.image, (i.rect.centerx, i.rect.centery))

        pygame.display.flip()


if __name__ == "__main__":
    main()