import Tkinter as tk
from Tkinter import *
from threading import *
from Puntos import *
from Figuras import *
from math import *
from Calculo_Circulo import *
from Calculo_Cuadrado import *
from Calculo_Rectangulo import *
from Calculo_Triangulo import *


class InterfaceFiguras(Thread):

    def __init__(self):
        self.root = Tk()
        self.Figura = Figuras()
        self.squart = Cuadrado()
        self.circle = Circulo()
        self.rectangle = Rectangulo()
        self.triangle = Triangulo()

        self.cadena = StringVar(self.root)
        #self.display = Entry(self.frame, textvariable=self.cadena)
        self.display = Label(self.root, textvariable=self.cadena, font=("Helvetica", 30))
        self.display.grid(row=0, column=1)
        self.root.geometry('500x500')

        self.buttonTrian = Button(self.root, text="Triangulo")
        self.buttonTrian.bind("<Button-1>", self.areaTri)
        self.buttonTrian.grid(row=2, column=1)
  
        self.buttonCuad = Button(self.root, text="Cuadrado")
        self.buttonCuad.bind("<Button-1>", self.areaCua)
        self.buttonCuad.grid(row=2, column=2)
            
        self.buttonCirc = Button(self.root, text="Circulo")
        self.buttonCirc.bind("<Button-1>", self.areaCir)
        self.buttonCirc.grid(row=2, column=3)

        self.buttonRec = Button(self.root, text="Rectangulo")
        self.buttonRec.bind("<Button-1>", self.areaRec)
        self.buttonRec.grid(row=2, column=4)

        self.punto1 = tk.StringVar(self.root)
        self.P1 = tk.Entry(self.root, textvariable = self.punto1)
        self.P1.grid(row=0, column=2)

        self.punto2 = tk.StringVar(self.root)
        self.P2 = tk.Entry(self.root, textvariable = self.punto2)
        self.P2.grid(row=0, column=4)

        self.punto3 = tk.StringVar(self.root)
        self.P3 = tk.Entry(self.root, textvariable = self.punto3)
        self.P3.grid(row=1, column=2)

        self.punto4 = tk.StringVar(self.root)
        self.P4 = tk.Entry(self.root, textvariable = self.punto4)
        self.P4.grid(row=1, column=4)

                
        etiqueta1 = tk.Label(self.root, text="Coordenada X1:")
        etiqueta1.grid(row=0, column=1)

        etiqueta2 = tk.Label(self.root, text="Coordenada Y1:")
        etiqueta2.grid(row=0, column=3)

        etiqueta3 = tk.Label(self.root, text="Coordenada X2:")
        etiqueta3.grid(row=1, column=1)

        etiqueta4 = tk.Label(self.root, text="Coordenada Y2:")
        etiqueta4.grid(row=1, column=3)

        self.varetiqueta5 = tk.StringVar()
        self.etiqueta5 = tk.Label(self.root, textvariable=self.varetiqueta5)
        self.etiqueta5.grid(row=4, column=2)

        self.varetiqueta6 = tk.StringVar()
        self.etiqueta6 = tk.Label(self.root, textvariable=self.varetiqueta6)
        self.etiqueta6.grid(row=4, column=3)

        self.root.mainloop()

        
    def tomarPuntos2(self):
        self.p1 = Punto()
        self.p2 = Punto()
        self.p1.x = int(self.punto1.get())
        self.p1.y = int(self.punto2.get())
        self.p2.x = int(self.punto3.get())
        self.p2.y = int(self.punto4.get())

    def areaTri(self, event):
        self.tomarPuntos2()
        self.triangle.setPuntos(self.p1,self.p2)
        self.triangle.calcularAreaTriangulo()
        self.triangle.calcularPerimetroTriangulo()
        self.varetiqueta5.set(self.triangle.area)
        self.varetiqueta6.set(self.triangle.perimetro)

    def areaCua(self, event):
        self.tomarPuntos2()
        self.squart.setPuntos(self.p1,self.p2)
        self.squart.calcularAreaCuadrado()
        self.squart.calcularPerimetroCuadrado()
        self.varetiqueta5.set(self.squart.area)
        self.varetiqueta6.set(self.squart.perimetro)

    def areaCir(self, event):
        self.tomarPuntos2()
        self.circle.setPuntos(self.p1,self.p2)
        self.circle.calcularAreaCirculo()
        self.circle.calcularPerimetroCirculo()
        self.varetiqueta5.set(self.circle.area)
        self.varetiqueta6.set(self.circle.perimetro)
    
    def areaRec(self, event):
        self.tomarPuntos2()
        self.rectangle.setPuntos(self.p1,self.p2)
        self.rectangle.calcularAreaRectangulo()
        self.rectangle.calcularPerimetroRectangulo()
        self.varetiqueta5.set(self.rectangle.area)
        self.varetiqueta6.set(self.rectangle.perimetro)

app = InterfaceFiguras()
