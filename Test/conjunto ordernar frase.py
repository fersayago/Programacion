"""
<>

>

<
"""
frase = "Hola que tal que como que estas"

listaFrase = frase.split()

conj = set()

for elem in listaFrase:
    conj.add(elem)

respuesta = list(conj)

respuesta.sort(key= lambda x: len(x), reverse=True)
    

print(respuesta)
