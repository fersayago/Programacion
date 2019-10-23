#Ejercicio 2 de la practica 7
# Desarrollar una función que reciba un número binario y lo devuelva convertido a base decimal.

# we need to keep track of the current string,
# the power of two, and the total (decimal)
def placeToInt (str, pow, total):
    # if the length of the string is one,
    # we won't call the function anymore
    if (len(str) == 1):
        # return the number, 0 or 1, in the string
        # times 2 raised to the current power,
        # plus the already accumulated total
        return int(str) * (2 ** pow) + total
    else:
        # grab the last digit, a 0 or 1
        num = int(str[-1:])
        # the representation in binary is 2 raised to the given power,
        # times the number (0 or 1)
        # add this to the total
        total += (num * (2 ** pow))
        # return, since the string has more digits
        return placeToInt(str[:-1], pow + 1, total)



# test case
# appropriately returns 21
print(placeToInt("1001", 0, 0))