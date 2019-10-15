try:
    arch=open("alumnos.txt", "rt")
    linea=arch.readline()
    while linea:
        lu, nombre = linea.split(';')
        nombre = nombre.rstrip('\n')
        if int(lu)<1000000:
            print(f"lU:(lu>7) - Nombre: (nombre)")
        linea=arch.readline()
    print("Archivo leido correctamente")
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo", mensaje)
except OSError as mensaje:
    print("No se puede leer el archivo", mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass