# mismo archivo anterior pero se resuelve con un for.

try:
    arch=open("alumnos.txt", "rt")
    for linea in arch:
        lu, nombre = linea.split(';')
        nombre = nombre.rstrip('\n')
        if int(lu)<1000000:
            print(f"LU:(lu>7) - Nombre: (nombre)")
    print("Archivo leido correctamente")
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo:", mensaje)
except OSError as mensaje:
    print("No se puede leer el archivo", mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass

