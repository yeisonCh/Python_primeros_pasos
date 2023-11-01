# en python no tenemos el switch
# el bucle for puede  recorres una lista, una tupla, cadena de texto etc


# EN UN BUCLE FOR DE PYTHON LA VARIABLE (i) O CUALQUIER OTRO NOMBRE 
# LA VARIABLE TOMA EL VALOR DEL ELEMENTO DE LA LISTA, TUPLA O CUALQUIER ELEMTO QUE LE PASEMOS 


#el for le asigna a i el valor del elemento en este caso 1,2,3
for i in [1,2,3]: # en este caso lo lee como posición 0,1,2 o elementos 
	print("Hola")

#recorrer el bucle for con listas con salto de linea
for i in ["Primavera", "Verano", "Otoño", "Invierno"]:
	print(i)

#recorrer el bucle for en listas sin salto de linea
for i in ["Pildoras", "Informaticas", 3]:
	print(i, end=" ")
print("")


#recorrer el bucle for con cadena de texto
email=False
for i in "wilson@pildorasinformaticas.es":
	if(i=="@"):
		email=True
if email==True:
	print("Email es correcto")
else:
	print("El email no es correcto")


#recorrer el bucle for con cadena de texto ingresando datos por consola
email=False
miemail=input("Ingrese tu direccion de correo electronico: ")

for i in miemail:
	if(i=="@"):
		email=True
if email==True:
	print("Email es correcto")
else:
	print("El email no es correcto")


#recorrer el bucle for con cadena de texto ingresando datos por consola
contador=0
miEmail=input("Ingrese tu direccion de correo electronico: ")
for i in miEmail:
	if(i=="@" or i=="."):
		contador=contador+1
if contador==2:
	print("Email es correcto")
else:
	print("El email no es correcto")



#recorrer el bucle for con el tipo range
# RANGE nos devulve un arreglo de cinco elementos 

for i in range(5):
	print(i)