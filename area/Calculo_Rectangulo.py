from Puntos import *
from Figuras import *
from math import *

class Rectangulo(Figuras):

    
    def calcularAreaRectangulo(self):
        p3 = Punto()
        p3.x = self.p1.x
        p3.y = self.p2.y
        self.area = "El area del Rectangulo es: " + str(p3.CalcularDistancia(self.p1) * p3.CalcularDistancia(self.p2))

    def calcularPerimetroRectangulo(self):
        p3 = Punto()
        p3.x = self.p1.x
        p3.y = self.p2.y
        self.perimetro ="El perimetro del Rectangulo es: " + str((2 * p3.CalcularDistancia(self.p1)) +(2 * p3.CalcularDistancia(self.p2)))

