from Puntos import *
from Figuras import *
from math import *

class Circulo(Figuras):

    
    def calcularAreaCirculo(self):
        p3 = Punto()
        p3.x = self.p1.x
        p3.y = self.p2.y
        self.area = "El area del Circulo es: " + str(pi * p3.CalcularDistancia(self.p1) * p3.CalcularDistancia(self.p2))

    def calcularPerimetroCirculo(self):
        p3 = Punto()
        p3.x = self.p1.x
        p3.y = self.p2.y
        self.perimetro ="El perimetro del Circulo es: " + str((2 * pi * p3.CalcularDistancia(self.p1)))

