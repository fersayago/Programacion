def aDecimal (num):
    if len(num) == 1:
        return int(num)
    else:
        primer_digito = int(num[0])
        resto = num[1:]

        return (primer_digito * (2 ** (len(num)-1))) + aDecimal(resto)





print(aDecimal("10011"))