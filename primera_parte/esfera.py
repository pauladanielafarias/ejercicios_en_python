# esfera.py
# Ejercicio 1.13: El volúmen de una esfera

'''
En tu directorio de trabajo, escribí un programa llamado esfera.py 
que le pida al usuario que ingrese por teclado el radio r de una esfera y 
calcule e imprima el volumen de la misma. Sugerencia: recordar que el volúmen de una esfera es 4/3 πr^3.

Finalmente, ejecutá el programa desde la línea de comandos para responder 
¿cuál es el volumen de una esfera de radio 6?
'''

import math
radio= int(input("Escribe el radio de una esfera: "))


volumen= (4/3 * math.pi) * (radio * radio * radio)

print("El volúmen de tu esfera es",volumen)

#--------------------------------------------
# input: 6
# output: El volúmen de tu esfera es 904.7786842338603