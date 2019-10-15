#convertir a mayusculas el contenido del archivo "notas.txt"
# como los archivos de texto no se pueden alterar crearemos una version

try:
    entrada = open("notas.txt","rt")
    salida= open("notas2.txt","wt")
    k = 0
    for linea in entrada:
        salida.write(linea.upper())
        k = k + 1

except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo", mensaje)
except OSError as mensaje:
    print("ERROR", mensaje)
else:
    print("Copia finalizada. Lineas copiadas:", k)
finally:
    try:
        entrada.close()
        salida.close()
    except NameError:
        pass