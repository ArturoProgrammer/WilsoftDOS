import sys
import os
from tui import sys_declarations

startgui = sys.argv[1]      # Autorizacion para iniciar el sistema                  (-y/-c)
ioaccess = sys.argv[2]      # Permiso para usar Inputs y Outputs del sistema        (-y/-c)
guimode = sys.argv[3]       # Modo en el que se ejecutara la GUI: Secure / Normal   (-s/-n)
hddaccess = sys.argv[4]     # Permiso para escribir datos en el dico duro           (-y/-c)



# PATH de los programas principales
DefaultAppList = {
	"settings" : "../../programs_/settings_paf.py"
	"web_browser" : "../../programs_/web_browser_paf.py"
}

# Ciclo del proceso principal del sistema
while startgui == "-y":
    if guimode == "-n":
        print("OS en modo normal sin gui activada")
    elif guimode == "-s":
    	# En este modo solo se permiten usar las aplicaciones por default del sistema
        print("OS en modo seguro con gui activada")
else:
    print("OS No ejecutado")
    sys.exit()



class SystemInOut (sys_declarations.Sys_Buses()):
	"""docstring for SystemInOut"""
	def __init__(self):
		super(SystemInOut, self).__init__()
		insysL1 = [1000, 1001, 1002, 1003, 1004]
		insysL2 = [2000, 2001, 2002, 2003, 2004]
		insysL3 = [3000, 3001, 3002, 3003, 3004]
		insysL4 = [4000, 4001, 4002, 4003, 4004]
		
		outysL1 = [1000, 1001, 1002, 1003, 1004]
		outysL2 = [2000, 2001, 2002, 2003, 2004]
		outysL3 = [3000, 3001, 3002, 3003, 3004]
		outysL4 = [4000, 4001, 4002, 4003, 4004]

		"""
		In & Out del sistema

		Inputs:
		-IN1000     -IN2000     -IN3000     -IN4000
		-IN1001*    -IN2001     -IN3001     -IN4001
		-IN1002     -IN2002     -IN3002*    -IN4002*
		-IN1003     -IN2003*    -IN3003     -IN4003
		-IN1004*    -IN2004     -IN3004     -IN4004

		Outputs
		-OUT1000     -OUT2000    -OUT3000     -OUT4000
		-OUT1001*    -OUT2001    -OUT3001     -OUT4001
		-OUT1002     -OUT2002    -OUT3002*    -OUT4002*
		-OUT1003     -OUT2003*   -OUT3003     -OUT4003
		-OUT1004*    -OUT2004    -OUT3004     -OUT4004

		Las I/O señaladas con un asterisco (*), son privadas al sistema
		"""
		self.__privatesInts = {
			"pi1" : insysL1[1],
			"pi2" : insysL1[4],
			"pi3" : insysL2[3],
			"pi4" : insysL3[2],
			"pi5" : insysL4[2]
		}
		
		self.__privatesInts = {
			"po1" : outsysL1[1],
			"po2" : outsysL1[4],
			"po3" : outsysL2[3],
			"po4" : outsysL3[2],
			"po5" : outsysL4[2]
		}