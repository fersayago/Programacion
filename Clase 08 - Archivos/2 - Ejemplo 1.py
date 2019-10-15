try:
    arch = open("alumnos.txt", "wt")
    lu = inpunt("LU? (enter para terminar):")
    while lu!="":
        nombre=input("nombre del alumno?")
        arch.write(lu+","+nombre+'\n')
        lu = input("LU? (enter para terminar:)")
    print("Archivo creado correctamente.")
except OSError as mensaje:
    print("No se puede grabara el archivo",)
    ####TERMINAR