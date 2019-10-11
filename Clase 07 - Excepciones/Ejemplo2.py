#Impedir que un programa falle debido a una divison por
#cero o por el ingreso de datos invalidos.
#El programa finaliza con un mensaje de error

try:
    a = int(input("Dividendo?"))
    b = int(input("Divisor?"))

    cociente = a // b
    resto = a % b
    print()
    print("Cociente:", cociente)
    print("Resto:", resto)

except ZeroDivisionError:
    print("No se puede dividir por cero")

except ValueError:
    print("Solo se permiten numeros enteros")

except:
    print("Error desconocido. Intente mas tarde.")