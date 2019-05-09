from Puntos import *
from Figuras import *
from math import *

class Triangulo(Figuras):

    
    def calcularAreaTriangulo(self):
        p3 = Punto()
        p3.x = self.p1.x
        p3.y = self.p2.y
        self.area = "El area del Triangulo es: " + str (((p3.CalcularDistancia(self.p1))* (p3.CalcularDistancia(self.p2))/2))

    def calcularPerimetroTriangulo(self):
        p3 = Punto()
        p3.x = self.p1.x
        p3.y = self.p2.y
        hipotenusa = self.p1.CalcularDistancia(self.p2)
        self.perimetro = "El Perimetro del Triangulo es: "+ str((p3.CalcularDistancia(self.p1)) + (p3.CalcularDistancia(self.p2)) + (hipotenusa))

