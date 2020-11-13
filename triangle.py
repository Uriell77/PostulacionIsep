#!/usr/bin/python
# -*- coding: latin-1 -*-
# Jueves 12 de Noviembre de 2020
# Test de Conocimiento del lenguaje de Programacion Python
# Luis Hermoso


# 4. Crea una clase para almacenar un triangulo, guardando sus tres lados (a, b y c) en campos privados. La clase tendra un metodo para calcular el area


class Triangulo():

    def __init__(self, a,b,c):
        #inicializa la clase con los valores de los lados privados
        self._a = a
        self._b = b
        self._c = c


    def area(self):
        # calculo del area de un triangulo conocidos sus tres lados
        p = (self._a + self._b + self._c)/2 #calculo del semiperimetro
        area = (p*(p - self._a) * (p - self._b) * (p - self._c))**(1.0/2) #calculo el area 
        return area

