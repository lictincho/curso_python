""""
Simula la tirada de dados. 
Cada vez que ejecutamos el programa, éste elegirá dos números aleatorios entre el 1 y el 6.
* imprimirlos en pantalla
* imprimir su suma
* preguntarle al usuario si quiere tirar los dados otra vez
"""

import random

def tirada_dados():    
    while True:
        primera= random.randint(1, 6)
        segunda= random.randint(1, 6)
        print (f"Sus numeros son: {primera} y {segunda}.")
        suma= primera + segunda
        print ("La suma de estos es:", suma)
        
        respuesta = input("Quiere tirar los dados otra vez ? si/no: ")
        
        if respuesta == "no":
            print ("Fin del programa.")
            break
        

tirada_dados()

