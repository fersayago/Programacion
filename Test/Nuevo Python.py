"""
<>

>

<
"""
lista = []

for i in range(20):
    lista.append(i+1)

diccionario = dict.fromkeys(lista, 0)

for elem in diccionario.items():
    diccionario[elem] = int(elem) ** 2
    
print(diccionario)
