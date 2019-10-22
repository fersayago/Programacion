"""
Un identificador en python es:
- una letra o guion bajo
- un identificador seguido por una letra, numero o guion bajo.

FUNCIONES RECURSIVAS:
la recursividad aplicada a la programacion se manifiesta en forma---


VENTAJAS:
    - Elegancia
    - Simplicidad

DESVENTAJAS:
    - Lentitud
    - Consumo de memoria.

Ejemplo factorial:
fact(n) = n * fact(n-1)


fact(0) = 1   (por convension)
"""

#FUNCION FACTORIAL

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

a = int(input("Ingrese un numero entero"))
print(" el factorial de", a, "es", fact(a))
