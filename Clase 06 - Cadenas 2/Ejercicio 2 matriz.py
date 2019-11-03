#Ejercicio para imprimir matriz F x C

def imprimirmatriz(mat):
    filas=len(mat)
    columnas=len(mat[0])
    elementos = filas * columnas
    f = 0
    c = 0
    for i in range (elementos):
        try:
            print("%3d" %mat[f][c], end="")
        except IndexError:
            f = f + 1
            c = 0
            print()
            print("%3d" %mat[f][c], end="")
        finally:
            c = c + 1
