class Punto:
    # solo crear un punto
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coords = [x, y]
    # da coordenadas
    def coordenadas(self):
        return self.coords
    # da un punto simetrico sobre un eje
    def simetrico(self, eje):
        sim = Punto(self.x, self.y)
        sim.coords[eje] += -1
        return sim
    # modulo del punto
    def modulo(self):
        sq = 0
        for i in self.coords:
            sq += i * i
        return sq ** 0.5
    # distancia entre dos puntos
    def distancia(self, otro):
        return abs(self.modulo() - otro.modulo())
