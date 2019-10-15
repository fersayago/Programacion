"""
Hasta ahora todo el mannejo de datos se realizo con variables o listas las cuales
se almacenan en la memoria principal

ARCHIVO:
Cualquiera sea el dispositivo en el que se almacenan los datos, lo que se estara guardando
sera siempre un archivo, lo cual es un conjunto de registros que van a tener el mismo tipo
de datos. Se almacenaran en un dispositivo auxiliar para preservar la info a traves del tiempo.

Archivo - es un conjunto de REGISTROS.

Registros - son un conjunto de CAMPOS.

CLASIFICACION DE ARCHIVOS:

1. Según el contenido de los registros:
- Archivos binarios
- Archivos de textos

2. Segun el sentido de la transferencia de datos:
- Archivos de entrada
- Archivos de salida
- Archivos de entrada/salida

3. Segun el modo de acceso:
- Archivos de acceso secuencial
- Archivos de acceso directo.

En Python se utiliza archivos de texto  generalmente. Es texto plano.

Cada linea es un registro por lo tanto cada registro puede tener un largo distinto a la de los
demas. Por lo que es necesario colocar un separador entre registros. 
Este separador se llama delimitador que se utiliza con la secuencia "\n" que representa el salto
de linea.

3 etapas en el trabajo de archivo:
--- Apertura---
se establecen los canales de comunicación con el dispositivo donde reside el archivo y
se reserva memoria para los buffers. se realiza con la función open(). El modo de apertura esta
formado por uno o dos caracteres:
PRIMER CARACTER
r(read): abre el archivo en modo de entrada (lectura solamente).
w(write): se abre el archivo en modo de salida (para grabación solamente)
a(append): abre en modo salida (grabacion solamente), y agregado de registros. la diferencia
con write es que si el archivo existe no lo destruye, sino que las grabaciones se haran al
final de los datos actuales.
SEGUNDO CARACTER
t(texto)
b(binario)
Si la apertura tuvo exito, devuelve un objeto archivo, si ocurre algun problema, se produce
una excepción.

--- Procesamiento ---
Consiste en realizar lecturas y grabaciones sobre el mismo. Existen 2 maneras distintas para
grabar y 3 para leer. Todas se realizan con metodos.

Metodos de grabación:
<arch>.write(<str>):
<arch>.writelines(<lista>):

Metodos de lectura:
<arch>.read([<n>]): Si no se le pasa un parametro devuelve todo en un string lo cual es un peligro con archivos grandes.
Conviene trabajar con 1 o 2 archivos por vez pero no todo el archivo dentro de la memoria. Una posibilidad es esscribir
un 1 como parametro, para leer un caracter por vez.
<arch>.readline(): Lee de una linea por vez.

--- Cierre ---
Se revierte todo lo que se hizo en la apertura.
Se cierran los canales de comunicacion con el dispositivo y se liberan los buffers, grabando
cualquier registro pendiente que pudiera haber.

Se utiliza el metodo close() de la variable que representa al archivo: arch.close()

Debido a la importancia del cierre, se suele realizar en la clausula finally



SE PUEDE REALIZAR TODA LA PRACTICA 6
"""
