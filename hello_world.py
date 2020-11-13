#!/usr/bin/python
# -*- coding: latin-1 -*-
# Jueves 12 de Noviembre de 2020
# Test de Conocimiento del lenguaje de Programacion Python
# Luis Hermoso


# 1. Escribe una funcion que devuelva la cadena "¡Hola, mundo!"; esta debera requerir 2 parametros tipo cadena, "Hola" y "Mundo", tambien deberas realizar un print de la cadena devuelta


def hola_mundo(Hola, Mundo):
    #imprime una cadena conformada por dos parametros con el formato "¡Hola, mundo!"
    Hola = Hola.capitalize()# el resultado debe tener el primer caracter mayuscula
    Mundo = Mundo.lower() # la segunda entrada todo es minuscula
    print('¡{}, {}!'.format(Hola, Mundo))

