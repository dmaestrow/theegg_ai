#!/usr/bin/python
#TAREA21 Fraccion irreducible para x ={0,0001 y 0,9999} (4 cifras decimales)
#   Un programa que dado un numero introducido entre 0,0001 y 0,9999 (no mas de 4 cifras decimales), obtenga y muestre la correspondiente fraccion irreducible.
#   A partir de explicacion en http://www.nachocabanes.com/retos/reto.php?n=013:
#   "Solucion simple y rapida: partir del numero expresado en forma de fraccion y dividir numerador y denominador tantas veces como se puedan entre 2 y entre 5 (porque son los unicos numeros primos)". 

import sys


#************************ Function **************************************
def get_irreducible_fraction(x,num_digits=4):

    denominator = int(pow(10,num_digits))
    numerator = int(x*denominator)

    for dc in [2,5]:
        while(numerator%dc==0  and denominator%dc==0):
            numerator = numerator/dc
            denominator = denominator/dc
                
    return [numerator,denominator]
    
#*************************** Test script ***********************************

# count input parameters
nargin = len(sys.argv)

# use default values if no input parameters have been entered

if(nargin<3):
    num_digits = 4
else:
    num_digits = int(sys.argv[2])

if(nargin<2):
    import random
    x = round(random.random(),num_digits);
else:
    x = round(float(sys.argv[1]),num_digits);


# compute and show result
fract = get_irreducible_fraction(x, num_digits)

print ("x = "+str(x))
print ("%d/%d " %(fract[0], fract[1]))

    
    
