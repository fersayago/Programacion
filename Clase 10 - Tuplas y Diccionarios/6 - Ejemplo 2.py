#Ingresar una frase por teclado y mostrar listado ordenado alfabeticamente omitiendo
#palabras repetidas mostrando en cada palabra la cantidad de veces que se encontraba
#en la frase original.

frase = input("Ingrese una frase:\n")

listadepalabras = frase.split()
dic={}

for palabra in listadepalabras:
    if palabra not in dic:
        dic[palabra] = 1

    else:
        dic[palabra] = dic[palabra] + 1

listado = []

for p in dic:
    listado.append(">"+p+":"+str(dic[p])+"veces")

listado.sort()

for linea in listado:
    print(linea)