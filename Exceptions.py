# Captura o control de excepción
# Intenta hacer esto y en caso de que no
# Ejecuta el resto del código
# La linea de return num1/num2 es suceptible a fallar
# Excepcion ValueError

def suma(num1,num2):
	return num1+num2

def resta(num1,num2):
	return num1-num2

def multiplica(num1,num2):
	return num1*num2

def divide(num1,num2):
	try:
		return num1/num2
	except ZeroDivisionError:
		print("No se puede dividir entre 0")

		return "Operación errónea"

while True:
	try:

		op1=(int(input("Introduce el primer numero: ")))
		op2=(int(input("Introduce el segundo numero: ")))
		break;

	except ValueError:
		print("Los valores introducidos no son correctos. Intentalo de nuevo")

operacion=input("Introduce la operación a realizar (suma, resta, multiplica, divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print("Operación no contemplada")

print("Operación ejecutada. Continuación  de ejecución del programa ")