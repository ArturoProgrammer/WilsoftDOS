import os
import datetime


def name(program):
    """Nombre del mensaje"""
    # Se pasa como argumento el nombre del programa que solicita el mensaje
    return program + str(datetime.date.today()) + "msg.vbs"

def createmsg(app_msg, pname):
	"""Crea el mensaje VBS"""
	messagefile = open(name(pname), "w")
	messagefile.write('MsgBox("' + app_msg + '")')
	messagefile.close()

	subprocess.call(["start", name()], shell=True) # Ejecuta el mensaje que se creo posteriormente


class Sys_buses:
	"""docstring for Sys_buses"""
	def __init__(self, bwtype):
		super(Sys_buses, self).__init__()
		self.autoStrong = True
		self.busWidth_default = bwtype

		if bwtype >= 2800:
			createmsg("El bus de datos se ha sobrecargado totalmente!", "Main System Proccess")

		self.busWidth_min = 900
		self.busWidth_max = 2800