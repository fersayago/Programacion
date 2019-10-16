# Practica 6 ejercicio 4

try:
    arch = open("Armenia.txt","rt")
    for linea in arch:
        ApellidoNombre = linea.split(',')
        ApellidoNombre = nombre.rstrip('\n')
