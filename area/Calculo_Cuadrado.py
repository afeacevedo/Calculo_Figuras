from Puntos import *
from Figuras import *
from math import *

class Cuadrado(Figuras):

    
    def calcularAreaCuadrado(self):
        p3 = Punto()
        p3.x = self.p1.x
        p3.y = self.p2.y
        self.area = "El area del Cuadrado es: " + str(p3.CalcularDistancia(self.p1) ** 2)

    def calcularPerimetroCuadrado(self):
        p3 = Punto()
        p3.x = self.p1.x
        p3.y = self.p2.y
        self.perimetro = "El perimetro del Cuadrado es: " + str (4 * p3.CalcularDistancia(self.p1))

