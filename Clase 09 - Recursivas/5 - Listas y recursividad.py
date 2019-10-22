# FUNCION QUE IMPRIME LISTA

lista =[]

def imprimirlista(lista, inicio=0):
    if inicio < len(lista):
        print(lista[inicio], end=" ")
        imprimirlista(lista, inicio+1)

imprimirlista(lista)


#FUNCION QUE BUSCA MAYOR EN UNA LISTA

def buscarmayor(lista, inicio=0):
    if inicio < len(lista)-1:
        actual = lista[inicio]
        mayor = buscarmayor[lista, inicio+1]
        return actual if actual > mayor else mayor
    else:
        return lista[-1] #ultimo elemento

maximo = buscarmayor(lista)