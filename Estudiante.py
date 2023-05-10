from Persona import Persona

class Estudiante(Persona):
    def __init__(self):
        pass


    def dibuj_aula(self, pant, tx, ty, mesx, mesy): #  tx=3, ty=5, mesx=70, mesy = 210
        self.dibuj_suelo(pant, 0, 0)
        self.dibuj_tarima(pant, 3, 5)
        self.dibuj_puerta(pant)
        self.dibuj_mesa_prof(pant)
        # self.dibuj_mesa(pant, mesx, mesy)
        # for i in range(2):
            # for j in range(5):
                # if j == 0:
                    # self.dibuj_mesa(pant, mesx, mesy)
                # else:
                    # self.dibuj_mesa(pant, mesx, mesy)
                # mesy += 100
            # mesx += 280
            # mesy = 210