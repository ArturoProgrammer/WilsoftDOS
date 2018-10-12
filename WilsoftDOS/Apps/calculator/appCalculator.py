import sys
import cientificsOperations

def main ():
	print("\n" + "Calculadora".center(50, "=") + "\n")
	print("""
a) Suma (+)
b) Resta (-)
c) Multiplicacion (*)
d) Division (/)
e) Elevar al cuadrado
f) Elevar al cubo
g) Raiz cuadrada 
h) Exit
		""")
	request = str(input("Que quiere hacer: ").lower())
	operations(request)

# Operaciones aritmeticas
def operations (petition):
	if petition == "a":
		numA = int(input("\nIngrese el numero A: "))
		numB = int(input("Ingrese el numero B: "))

		val = numA + numB
		print("\nEl resultado es: {}".format(val))
		main()
	elif petition == "b":
		numA = int(input("\nIngrese el numero A: "))
		numB = int(input("Ingrese el numero B: "))

		val = numA - numB
		print("\nEl resultado es: {}".format(val))
		main()
	elif petition == "c":
		numA = int(input("\nIngrese el numero A: "))
		numB = int(input("Ingrese el numero B: "))

		val = numA * numB
		print("\nEl resultado es: {}".format(val))
		main()
	elif petition == "d":
		numA = int(input("\nIngrese el numero A: "))
		numB = int(input("Ingrese el numero B: "))

		val = numA / numB
		print("\nEl resultado es: {}".format(val))
		main()
	elif petition == "e":
		numA = int(input("\nIngrese el numero A: "))

		val = cientificsOperations.raiseToSquare(numA)
		print("\nEl resultado es: {}".format(val))
		main()
	elif petition == "f":
		numA = int(input("\nIngrese el numero A: "))

		val = cientificsOperations.raiseToCube(numA)
		print("\nEl resultado es: {}".format(val))
		main()
	elif petition == "g":
		numA = int(input("\nIngrese el numero A: "))

		val = cientificsOperations.arithmetiRaise(numA)
		print("\nEl resultado es: {}".format(val))
		main()
	elif petition == "h":
		sys.exit()
		
main()