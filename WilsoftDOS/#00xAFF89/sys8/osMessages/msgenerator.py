import subprocess
import sys
import datetime

"""
Clase diseñada para los desarrolladores.
Esta clase se incluye y se ejecuta en las aplicaciones.

Incluida en la libreria WilOSx86-64.hdla
"""

def name():
    """Nombre del mensaje"""
    program = sys.argv[1]   # Se pasa como argumento el nombre del programa que solicita el mensaje
    return program + str(datetime.date.today()) + "msg.vbs"

def createmsg(app_msg):
    """Crea el mensaje VBS"""
    messagefile = open(name(), "w")
    messagefile.write('MsgBox("' + app_msg + '")')
    messagefile.close()

    subprocess.call(["start", name()], shell=True) # Ejecuta el mensaje que se creo posteriormente

if __name__ == '__main__':
    code = sys.argv[2]
    createmsg(code)

# NOTE: Los argumentos requeridos para ejecutar el programa son:
# 1 (Nombre del programa que se esta ejecutando)
# 2 (Informacion que se va a mostrar en el mensaje)
