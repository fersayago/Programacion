# mismo archivo anterior pero se resuelve con un for.

try:
    arch=open("alumnos.txt", "rt")
    for linea in arch:
        lu, nombre = linea.split(';')
        nombre = nombre.rstrip('\n')
        if int(lu)<1000000:
            print(f"LU:(lu>7) - Nombre: (nombre)")
        print("Archivo leido correctamente")

        ####TERMINAR

