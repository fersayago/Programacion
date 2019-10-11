#Utilizar manejo de excepciones para continuar normalmente
#la ejecucion de una funcion luego de producido un error.


#funcion para ingresar un numero entero
def leerenter(mensaje="Ingrese un entero")

while True:
    try:
        n = int(input(mensaje))
        break
    except ValueError:
        print("Dato invalido.")
        print("Intente nuevamente")

return n

#Programa principal

while True:
    try:
        a = leerentero("Dividendo?")
        b = leerentero("Divisor?")
        cociente = a // b
        resto = a % b
        break
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
        print("Intente nuevamente")
print()
print("Cociente:", cociente)
print("Resto:", resto)