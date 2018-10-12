# -*- encoding: utf-8-*-

"""
El programa 'Main On Time' se encarga de controlar y ejecutar
las aplicaciones que el usuario quiera usar. Aqui se crean
las caches de los pogramas en ejecucion, los registros de las 
instrucciones que usaron, etc.

Se pueden ejecutar aplicaciones de Python y de Batch. Para Python
se usa un emulador virtual para ejecutarlas dentro del sistema.
"""

import sys
import subprocess


file_name = str(sys.argv[1]) # Se pasa como argumento el nombre del programa
print("Ejecutando " + file_name)

if file_name[8:] == ".py":
	subprocess.call(["python", file_name], shell=True)
elif file_name[8:] == ".bat":
	subprocess.call(["start", file_name], shell=True)
else:
	print("NO CODE FILE DETECTED")


def writeCacheData(filetowork, datainfo):
	"""Esta funcion sirve para escribir la cache de cada aplicacion cuando se ejecuta"""
	
	sfiletowork = str(filetowork)
	sdatainfo = str(datainfo)
	
	# Los archivos .oc son para almacenar datos de cache
	# Object Cache (.oc)
	
	namecachefile = sfiletowork + "CacheofData.oc"
	
	data = open(namecachefile, "w")
	data.write("data: {} ".format(sdatainfo)) # informacion a escribir
	data.close()

	subprocess.call(["start", "ocmover.bat", namecachefile], shell=True)

def closeProgram():
	sys.exit()

def startProgram():
	pass

writeCacheData(file_name, "81AABLA")