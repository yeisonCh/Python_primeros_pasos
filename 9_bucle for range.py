#recorrer el bucle for con el tipo range
# RANGE nos devulve un arreglo de cinco elementos 

for i in range(5):
	print(f"Valor de la variable {i}")
# podemos usar la letra f para conctenar un texto con una variable

print("modificar de donde debe empezar a contar y hasta donde  ejemplo 5,10")
for i in range(5,10):
	print(f"Valor de la variable {i}")
# podemos usar la letra f para conctenar un texto con una variable


print("tres argumantos desde donde inicia 5 hasta donde 50  para das saltos en este caso de tres en tres 3")
for i in range(5,50,3):
	print(f"Valor de la variable {i}")
# podemos usar la letra f para conctenar un texto con una variable


valido= False
email=input("introduce tu email")

for i in range(len(email)): #range nos devuelve la cantidad de elementos que introducimos y recorrera esas veces 
    if email[i]=="@": valido=True

if valido: 
	print("Email correcto")
else:
	print("Email incorrecto")