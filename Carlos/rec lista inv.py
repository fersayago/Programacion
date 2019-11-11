lista = [1,2,3,4,5,6]


def invLista(l):
    if len(l) == 1 or len(l) == 0:
        return l
    else:
        var = invLista(l[1:])
        var.append(l[0]) 
        return var




print(invLista(lista))
