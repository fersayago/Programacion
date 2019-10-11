#Impedir que un programa falle debido a una divison
#por cero
try:
    a = int(input("Dividendo?"))
    b = int(input("Divisor?"))

    cociente = a // b
    resto = a % b

    print()
    print("Cociente:", cociente)
    print("Resto:" resto)

except ZeroDivisionError:
    print("No se puede dividir por cero")

