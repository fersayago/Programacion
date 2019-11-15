# MaNo - Segundo Parcial, Tema 2

def hhmm2min(hora):
    """ Convierte un horario hhmm en minutos """
    hh = int(hora[:2])
    mm = int(hora[2:])
    return hh*60 + mm

def min2hhmm(minutos):
    """ Convierte minutos en horas y minutos """
    horas = minutos // 60
    min = minutos % 60
    return f"{horas:02} horas {min:02} minutos"
    

# Programa principal
try:
    diccionario = dict.fromkeys(range(1,32), 0)    # Diccionario de acumuladores por día. Se acumulará todo convertido a minutos.
    arch = open("mensuales.txt")
    k = 0
    for linea in arch:
        linea = linea.rstrip("\n")
        dia, numemp, nombre, he, hs = linea.split(";")
        entrada = hhmm2min(he)
        salida = hhmm2min(hs)
        tiempotrabajado = salida - entrada
        if tiempotrabajado<0:  # Turno noche, hora salida < hora entrada
            tiempotrabajado = 1440+tiempotrabajado
        diccionario[int(dia)] += tiempotrabajado
        k += 1
    print("Registros procesados:", k)
    print()
    lista = list(diccionario.items())  # Convertimos el diccionario en una lista para poder ordenarlo
    lista.sort(key=lambda x:x[1], reverse= True)      # Odenamos la lista por el segundo elemento de cada tupla
    for tupla in lista:
        print(f"Día {tupla[0]:2}: {min2hhmm(tupla[1])} trabajados")
except (FileNotFoundError, OSError) as error:
    print("ERROR:", error)
finally:
    try:
        arch.close()
    except NameError:
        pass