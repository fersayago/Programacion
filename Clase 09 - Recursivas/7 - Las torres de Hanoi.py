"""
Es un pasatiempo que se presento en Europa en 1883

El entretenimiento intenta reproducir una tarea que, segun la leyenda, vienen
desarrollando los monjes del templo de Brahma en la India
"""

def mover(n, origen, destino, aux):
    if n>0:
        mover(n-1, origen, aux, destino)
        print("Muevo el disco", n, "de", origen, "a", destino)
        mover(n-1, aux, destino, origen)

#Programa principal

discos = int(input("Cantidad de discos?"))

mover(discos, 1, 3, 2)