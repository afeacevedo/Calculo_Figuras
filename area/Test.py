from Puntos import *
from Calculo_Rectangulo import *
from Calculo_Triangulo import *
from Calculo_Cuadrado import *
from Calculo_Circulo import *

p1 = Punto()
p2 = Punto()
p1.x = 1
p1.y = 4
p2.x = 5
p2.y = 2

r = Rectangulo()
r.setPuntos(p1,p2)
r.calcularAreaRectangulo()
r.calcularPerimetroRectangulo()
print (r.area,r.perimetro)

t = Triangulo()
t.setPuntos(p1,p2)
t.calcularAreaTriangulo()
t.calcularPerimetroTriangulo()
print (t.area,t.perimetro)

c = Cuadrado()
c.setPuntos(p1,p2)
c.calcularAreaCuadrado()
c.calcularPerimetroCuadrado()
print (c.area,c.perimetro)

ci = Circulo()
ci.setPuntos(p1,p2)
ci.calcularAreaCirculo()
ci.calcularPerimetroCirculo()
print (ci.area,ci.perimetro)


