while True:
    try:
        mes = int (input("Ingrese el mes:"))
        assert 1 <= mes <= 12
        break
    except ValueError:
        print("Solo se permiten numeros")
    except AssertionError:
        print("El mes debe estar entre 1 y 12")
    print("INtente nuevamente")

print("El mes ingresado es", mes)