#!/usr/bin/python
# -*- coding: latin-1 -*-
# Jueves 12 de Noviembre de 2020
# Test de Conocimiento del lenguaje de Programacion Python
# Luis Hermoso


# 2. Deberas convertir un numero en una cadena que contenga sonidos de gotas de agua correspondientes a ciertos factores potenciales. Un factor es un numero que se divide uniformemente en otro numero, sin dejar resto.
#Las reglas de las gotas son para numeros determinados:
#Si tiene 3 como factor, agregue 'Plic' al resultado.
#Si tiene 5 como factor, agregue 'Plac' al resultado.
#Si tiene 7 como factor, agregue 'Ploc' al resultado.
#Si no tiene 3, 5 o 7 como factor, el resultado deben ser los digitos del numero.


def got(n):
    #conversion a gotas
    res = ''
    factores = {3:'Plic',5:'Plac',7:'Ploc'}

    for i in factores:
        if n%i == 0: # calculo del factor igual a 0
            res =res + factores[i]# formacion de la cadena segun el indice i en factores
        else:
            next # si el calculo no es 0 pasa al siguiente factor
    if res == '': #comprobacion de cadena vacia si ningun factor es 0 retorna el numero dado
        return n
    else:
        return res # retorna el resultado de la cadena si no es vacia
