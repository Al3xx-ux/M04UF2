#!/usr/bin/python3

version = 0.5

title_app = "playlist v"+str(version)

print(title_app)

print("-"*len(title_app))


def saluda ():
	print ("HoLa")


def suma(num1,num2):
	return num1+num2



def despiden (quien="jacinto"):
	print("Estas despedido", quien)



def return_multiple ():

	uno = 1 
	dos = 2
	return uno,dos

if False:
	print("Cierto")
else:
	print("Falso")

primero =5
segundo = 5

if primero < segundo:
	print ("El primero es mas pequeño que el segundo")
elif primero > segundo:
	print("El primero es mas grande que el segundo")
else:
	print("Son igules")

contador = 10
while contador > 0:
	print(contador)
	contador -= 1

print("-----------")
for num in range(1,11):
	#print(num)
	pass
personas = ["jacinto", "Alex", "Rafa"]

print (personas[1])



personaje = {
	"nombre": "PACO",
	"edad": 33,
	"pelo": "marron",
	
}

print("Personaje:", personaje["nombre"])

for dato in personas:
	print(">",dato)



for clave in personaje:
	print (">>",personaje [clave])


for clave, valor in personaje.items():
	print(">>>", clave, valor)


saluda()



resultado = suma(3, 4)

print(resultado)
despiden("ALEX")

valor1, valor2 = return_multiple()
print("Valores", valor1, valor2)



nombre = input("Tu nombre\n")
print (nombre)
