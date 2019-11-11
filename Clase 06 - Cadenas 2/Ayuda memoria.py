"""
APLICABLES A VARIABLES O CONSTANTES:

<str>.isalpha(): 
T o F si caracteres son alfabeticos.

<str>.isdigit(): 
T o F si caracteres son numericos.

<str>.isalnum(): 
T o F si caracteres son alfabeticos o numericos.

<str>.isupper(): 
T o F si caracteres estan en mayuscula. (ignora caract. no alfabeticos)

<str>.islower(): 
T o F si caracteres estan en minuscula.

<str>.upper(): 
Devuelve convertida a mayusculas (ignora caract. no alfabeticos).

<str>.lower(): 
Devuelve convertida a minusculas.

<str>.capitalize(): 
Devuelve convirtiendo el primer caract. de la cadena a mayusculas y el resto a minusculas.

<str>.title(): 
Devuelve convirtiendo a mayusculas el primer caracter de cada palabra y el resto a minusculas.

<str>.center(<ancho>[,<relleno>]): 
Devuelve con el ancho especificado, el resto de la cadena se rellan con espacios o el caracter
asignado, si es que se le asigna uno.

<str>.ljust(<ancho>[,<relleno>]): 
Devuelve alineada a la izquierda con el ancho esp, el resto de la cadena se rellena con espacios
o el caracter asignado, si es que se le asigna uno.

<str>.ljust(<ancho>[,<relleno>]): 
Devuelve alineada a la izquierda con el ancho esp, el resto de la cadena se rellena con espacios
o el caracter asignado, si es que se le asigna uno.

<str>.rjust(<ancho>[,<relleno>]): 
Devuelve alineada a la derecha con el ancho esp, el resto de la cadena se rellena con espacios
o el caracter asignado, si es que se le asigna uno.

<str>.zfill(<ancho>):
Devuelve alineada a la derecha con el ancho especificado, El comienzo de la cadena se rellana
con ceros.

<str>.lstrip([<cad>]):
Elimina los caracteres de cad al comienzo del string. Si cad se omite se eliminan los espacios.

<str>.rstrip([<cad>]):
Elimina los caracteres de cad al final del string. Si cad se omite se eliminan los espacios.

<str>.strip([<cad>]):
Elimina los caracteres de cad de ambos extremos del string. Si cad se omite se eliminan los espacios.

<str>.find(<cad>[,<inicio>[,<fin>]]):
Busca la primera posicion de cad dentro del string, devolviendo posicion. Si no se encuentra, provoca
un error. Inicio y fin se utilizan para indicar subindices donde comienza y termina la busqueda.

<str>.rfind(<cad>[,<inicio>[,<fin>]]):
Busca la ultima posicion de cad dentro del string, devolviendo posicion. Si no se encuentra, provoca
un error. Inicio y fin se utilizan para indicar subindices donde comienza y termina la busqueda.

------ METODO FORMAT ------

<str>.format(<datos>):
Sirve para darle formato a la salida impresa. La cadena str debe contener marcadores de posicion
{} donde se insertaran los datos.
"""
dia = 20
mes = "Abril"
fecha = "Hoy es {} de {}".format(dia,mes)
print(fecha)
"""
Se pueden usar numeros para indicar la posicion en la que se colocaran los datos, si los numeros se omiten
se usa el orden posicional.
"""
lluvia = "En {1} llovieron {0} dias".format(dia, mes)
print(lluvia)
"""
Para alinear numeros y cadenas se puede colocar un numero dentro de las llaves para representar el ancho,
es necesario escribir dos puntos antes del numero.

a = 15
cad = '*{:5}*'.format(a)
print(cad)

En forma predeterminada los numeros se alinean a la derecha y las cadenas a la izquierda. Para modificar
esto se usan los simbolos <, >, ^, entre los dos puntos y el ancho.

c = "*{:=^8}*".format("Hola") # *==Hola==*

Para regular la cantidad de decimales deseados se escribe un punto la cantidad de decimales deseados y
la letra f.

c= "{:.2f}".format(3.1416)   # 3.14

------ F-String ------

Son formatted strings. Consisten en cadenas normales precedidas por la letra f.
Donde deben insertarse los datos se escribren las variables correspondientes, encerradas entre llaves.

Tambien pueden escribirse expresiones en lugar de variables o invocar funciones y metodos.

Todas las posibilidades del metodo format() tambien estan presentes en los f-strings.
"""

nombre = "Bianca"

nota = 8

infNota = f"Hola {nombre:-^10}. sacaste un {nota}"

print(infNota)

print(f"{2 * 40}")

