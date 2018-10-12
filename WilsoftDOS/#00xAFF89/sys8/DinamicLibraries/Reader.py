import os
import sys

"""
Proceso de ejecucion de una dla

1 -> Se envian una orden de ejecucion con los parametros preestablecidos
2 -> Se localiza el codigo a ejecutar
3 -> Se ejecuta el codigo en el metodo deseado


Metodos de ejecucion:
- Maquina de codigo virtual * En desarrollo
	> Es un compilador desarrollado para codigo de Python y 
	  adaptado para el uso del script de tipo DLA/HDLA.
- Archivo espontaneo * En desarrollo
	> Es un archivo creado a base de rompecabezas, con el
	  archivo indexer. En el indexer, se encuentran las
	  ordenes de como se debe estructurar el codigo de 1 o
	  mas DLA/HDLA.

Diferencia:
* Las DLA se ejecutan mientras un programa esta en ejecucion.
  El uso de una DLA es dinamico, solo cuando se solicita una
  funcion de cierta libreria para hacer funcionar el programa.
  Es una libreria cerrada.

* Las HDLA (Header DLA) son similares a las DLA, con la
  diferencia de que estas se usan como una libreria abierta al
  programador para el desarrollo de programas. Es como un modulo
  de Python, o una libreria de C/C++. Es una libreria abierta.
"""

delete = lambda fname : os.remove(fname)

def read_DLA_code (dlafname, block, referential):
	"""
	Lee el codigo deseado de una dla y posteriormente lo ejecuta.
	Argumentos: dlaname (nombre del archivo), block (bloque en el que se encuentra), referential (referencial del codigo)
	"""

	file = open(dlafname, 'r')

	for line in file.read():
		if line.lower == """@[ 'referential' : '{ref}' ]""".format(ref = referential):
			print('REFERENCIAL LOCALIZADO')
		else:
			print('REFERENCIAL NO LOCALIZADO')
		print(line) 	# Imprime la linea actual que se esta leyendo

	file.close()


def read_HDLA_code (hdlafname, block, referential):
	pass