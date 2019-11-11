lista = [1, 2, 3, 4, 10, 6, 5, 8]

def calcMaximo(l):
    if len(l) == 1:
        return l[0]
    else:
        if l[0]> calcMaximo(l[1:]):
            return l[0]
        else:
            return calcMaximo(l[1:])





print(calcMaximo(lista))