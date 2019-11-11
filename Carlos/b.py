# Programación I - Simulacro segundo parcial

try:    
    buscar = input("Palabra a buscar? ")
    reemplazar = input("Reemplazarla por? ")
    entrada = open("prueba.txt","rt")
    salida = open("notas2.txt","wt")
    cambios = 0
    for linea in entrada:
        # Se busca sobre una lista y se reemplaza sobre la cadena mediante rebanadas.
        # Esto se hace para evitar falsos positivos (detectar "venta" en "inventario" )
        lista = linea.split()
        while buscar in lista:
            inicio = linea.find(buscar)
            final = inicio+len(buscar)
            
            
            linea = linea[:inicio]+reemplazar+linea[final:]
            cambios = cambios + 1
            # Borramos de la lista la palabra eliminada buscar mas repeticiones
            lista.remove(buscar)
        salida.write(linea)
except FileNotFoundError as error:
    print("Error al abrir los archivos:", error)
except OSError as error:
    print("Error fatal:", error)
else:
    print()
    print("Proceso finalizado.")
    print("La palabra '", buscar, "' fue reemplazada ", cambios, " veces.", sep="")
finally:
    try:
        entrada.close()
        salida.close()
    except NameError:
        pass