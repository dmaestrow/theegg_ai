# TAREA21 - Fracción irreducible

## Objetivo

Desarrollar un programa que dado un numero introducido entre 0,0001 y 0,9999 (no más de 4 cifras decimales), obtenga y muestre la correspondiente fracción irreducible.

## Contexto

Una fracción irreducible es una fracción en la que el numerador y el denominador no comparten factores en común,
de forma que no existe otra fracción equivalente que se pueda escribir en términos más sencillos. Por lo tanto,
obtener la fracción irreducible correspondiente a un numero dado se reduce a dividir el numerador y el denominador entre su máximo común divisor.

## Solución propuesta

Se ha implementado una función en python (`get_irreducible_fraction(x,num_digits=4)`) que calcula la fracción irreducible de un numero x a partir del algoritmo explicado en [1].

Esta función toma un número x y lo convierte a una representación en forma de fracción usando 10^num_digits como denominador.
Nótese que esta primera representación es valida para todos los números con num_digits cifras decimales (por defecto 4).
A continuación, la correspondiente fracción irreducible se halla explotando el hecho de que el 2 y el 5 son los únicos números primos divisores del denominador.
Esto permite hallar la solución simultaneamente dividiendo numerador y denominador entre cada uno de estos números (2 y 5) tantas veces como sea posible.


### Ejecución   

La función se ha implementado en un script en python que toma como argumento un numero de entrada y visualiza el resultado. 
En caso de no pasarle ningún número, el script llama a la función con un numero aleatorio dentro del rango estipulado. 

Para ejecutarlo basta con llamarlo desde línea de consola:

```
cd ~/EGG/repo/theegg_ai/tarea_21/
```



```

python main_tarea21.py 0.1995

```
o

```
python main_tarea21.py
```


Obteniendo a la salida el número aleatorio empleado y su correspondiente fracción irreducible, como por ejemplo:

```
x = 0.1995
```


```
399/2000
```
### Requisitos
Python 2.7.12 o 3.5.2 (probado en Ubuntu).

## Referencias
[1] http://www.nachocabanes.com/retos/reto.php?n=013.
