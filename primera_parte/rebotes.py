# rebotes.py
# Ejercicio 1.5: La pelota que rebota

""" 
# Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que 
# toca el piso salta 3/5 de la altura desde la que cayó. 
# Escribí un programa rebotes.py que imprima una tabla mostrando las alturas 
# que alcanza en cada uno de sus primeros diez rebotes.
"""

rebote=0
altura= 100
alturaNueva=0

while rebote<10:
    
    alturaNueva = float(altura * 3/5)
    altura = alturaNueva
    print(round(altura,4))

    rebote=rebote+1

#--------------------------------------------
# output: 
'''
60.0
36.0
21.6
12.96
7.776
4.6656
2.7994
1.6796
1.0078
0.6047
'''