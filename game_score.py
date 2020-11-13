#!/usr/bin/python
# -*- coding: latin-1 -*-
# Jueves 12 de Noviembre de 2020
# Test de Conocimiento del lenguaje de Programacion Python
# Luis Hermoso


# 3. Ahora deberas construir un componente de alta puntuacion para un juego clasico. Tu tarea es escribir metodos que devuelvan la puntuacion mas alta de la lista, la ultima puntuacion agregada y las tres puntuaciones mas altas.


class Score(list): # clase que hereda de lista

    def Max_Score(self):
        maximo = max(self) #funcion 'max()' de objetos iterables para determinar el mayor elemento
        return maximo


    def Ultima(self):
        ultima = self[-1] #ultimo elemento agregado a la lista iterada desde el fin
        return ultima

    
    def Tres_Altas(self):
        tres = sorted(self, reverse=True) # lista ordenada de mayor a menor y toma de los primeros 3 elementos
        return tres[:3]



