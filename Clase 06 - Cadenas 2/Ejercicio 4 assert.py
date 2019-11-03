palabra = input("ingrese una palabra:")

try:
    assert len(palabra)>5, "palabra muy corta"
    assert palabra.isalpha(), "Solo se permiten letras"
except AssertionError as mensaje:
    print(mensaje)