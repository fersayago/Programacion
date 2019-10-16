# TP6
## Ex. 4
### PROGRAMA PRINCIPAL ###
try:
    archivoEntrada = open("ENTRADA.txt", "rt")

    archivoSalidaArmenia = open("ARMENIA.txt", "wt")
    archivoSalidaItalia = open("ITALIA.txt", "wt")
    archivoSalidaEspaña = open("ESPAÑA.txt", "wt")

    for linea in archivoEntrada:
        apellidoNombre = linea.split(",")
        if apellidoNombre[0].upper().endswith("IAN", len(apellidoNombre[0])-3):
            archivoSalidaArmenia.write(linea)
        elif apellidoNombre[0].upper().endswith("INI", len(apellidoNombre[0])-3):
            archivoSalidaItalia.write(linea)
        elif apellidoNombre[0].upper().endswith("EZ", len(apellidoNombre[0])-2):
            archivoSalidaEspaña.write(linea)
        else:
            pass

except FileNotFoundError as msg:
    print("ADVERTENCIA:", msg)
except OSError as msg:
    print("ERROR:", msg)
else:
    print("FIN.")
finally:
    try:
        archivoEntrada.close()
        archivoSalidaArmenia.close()
        archivoSalidaItalia.close()
        archivoSalidaEspaña.close()
    except NameError as msg:
        pass
