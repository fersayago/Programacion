#Ejercicio 7 de la practica 7
"""
Dados dos números enteros no negativos, devolver el resultado de calcular el Máximo Común
Divisor (también llamado Divisor Común Mayor) basándose en las siguientes propiedades:

MCD(X, X) = X
MCD(X, Y) = MCD(Y, X)
Si X > Y => MCD(X, Y) = MCD(X–Y, Y).
"""

def MCD(num1, num2):
    if num1 == num2:
        return num1
    else:
        if num1 > num2:
            return MCD(num1-num2, num2)
        else:
            return MCD(num2, num1)


print(MCD(2000,104473))

