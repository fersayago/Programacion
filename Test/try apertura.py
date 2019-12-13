try:
    manejador = open("entradas.txt", "rt")
    
    cont = 1
    
    for lineas in manejador:
        #lineas = lineas.strip('\n')
        print(f"{cont:>3}. {lineas.rstrip().rstrip('.')}")
        cont += 1



except FileNotFoundError:
    print("No se encontró el archivo")

except OSError:
    print("error de sistema operativo")
    
finally:
    try:
        manejador.close()
    except:
        pass

"""
<>

>

<
"""

