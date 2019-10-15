"""
avanza automaticamente con cada operacion de lectura o escritura.
De esta manera el sistem conoce cual es el proximo registro a leer o grabar.

Al terminar la lectura el lector termina en el final del documento por lo que si queremos
volver a usarlo tenemos dos opciones:
1. Cerrar y volverlo a abrir. No recomendado debido al alto costo, se cierra el documento
y se tiene que volver a abrir
2. Utilizar el metodo seek(0): arch.seek(0)
Esto regresa el indicador de posicion al comienzo de los datos.



SI USAMOS FOR NO USAMOS readline
"""