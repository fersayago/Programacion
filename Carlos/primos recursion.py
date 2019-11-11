aChequear = int(input("Ingrese un numero para revisar si es primo:"))

""" FER
def esPrimo (num, cont, flag):
    if cont < num :
        if num % cont == 0:
            flag = True
    if cont == num:
        if flag == True:
            return flag
        if flag == False:
            return flag

    esPrimo(num, cont+1, flag)

if esPrimo(aChequear, 2 , False) == true:
    print("no es primo")
else:
    print("es primo")
"""

# CAR


def primoCar(num, cont):
    if num == cont:
        return True
    elif num % cont == 0 or num == 1:
        return False
    else:
        return primoCar(num, cont + 1)

if primoCar(aChequear, 2):
    print("es primo")
else:
    print("no es primo")


