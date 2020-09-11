# inclusive.py
# Ejercicio 1.29: Traductor (rústico) al lenguaje inclusivo

'''
Queremos hacer un traductor que cambie las palabras masculinas de una frase por su versión neutra. 
Como primera aproximación, completá el siguiente código para reemplazar todas las letras 'o' que figuren 
en el último o anteúltimo caracter de cada palabra por una 'e'. 
Por ejemplo 'todos somos programadores' pasaría a ser 'todes somes programdores'. 
'''



frase = input("Escribí la frase que quieras cambiar por su versión inclusiva: ")

palabras = frase.split()

frase_inclusiva=[]

for palabra in palabras:
    
    #letras que se van a usar como listas para que puedan ser unidas a otras listas
    e=["e"] 
    coma=[","]

    #palabra sea de una sola letra
    if len(palabra) == 1:
        palabra=palabra
    
    #palabra con coma al final
    elif palabra[-1]== ",":
        palabra=palabra.replace(",","") 
        
        #palabra con coma al final y con "o" en la última letra
        if palabra[-1] == "o":
            palabra = palabra[:-1].split()
            palabra = palabra + e + coma
            palabra = "".join(palabra)

        #palabra con coma al final y con "o" en la anteúltima letra
        elif palabra[-2] == "o":
            ultima_letra= list(palabra[-1])
            palabra = palabra[:-2].split()
            palabra = palabra + e + ultima_letra + coma
            palabra = "".join(palabra)
        
        #palabra solo con coma al final
        else:
            palabra=palabra + ","

    #palabra con "o" en la última letra
    elif palabra[-1] == "o":
        palabra = palabra[:-1].split()
        palabra = palabra + e
        palabra = "".join(palabra)
    
    #palabra con "o" en la anteúltima letra
    elif palabra[-2] == "o":
        ultima_letra= list(palabra[-1])
        palabra = palabra[:-2].split()
        palabra = palabra + e + ultima_letra 
        palabra = "".join(palabra)
    
    #el resto de las palabras
    else:
        palabra=palabra
    
    #union de todas las palabras en una frase
    frase_inclusiva.append(palabra)

#imprimir la frase a modo de string y no de listas (con el join)
print(" ".join(frase_inclusiva))


#--------------------------------------------
# input: todos somos programadores
# output: todes somes programadores