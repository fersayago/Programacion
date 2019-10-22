"""
TEOREMA FUNDAMENTAL DE LA RECURSIVIDAD:

"Todo problema que admita una solucion iterativa admite tambien una solucion recursiva y viceversa"

"""

#Prueba de escritorio para n=100

def imprimir(n):
    if n > 0:
        imprimir(n-1)
        print(n, end=" ")

imprimir(100)