#objeto string

"""
Metodos 

upper -> pasa todo a minusculas
lower -> pasa todo a mayusculas


"""

nombreUsuario=input("Introduce tu nombre de usuario: ")

print("el nombre es ", nombreUsuario.upper()) # para pasar a minusculas
print("el nombre es ", nombreUsuario.lower()) # para pasar a minusculas
print("el nombre es ", nombreUsuario.capitalize()) # para pasar a minusculas


edad = input("introduce la edad ")
print(edad.isdigit()) #devuelve si es un numero o no con un bolean


edad_usuario=input("Introduce tu edad por favor: ")

while(edad_usuario.isdigit()==False):
	print("debes introducir un valor númerico")
	edad_usuario=input("Introduce tu edad por favor: ")
	

if (int(edad_usuario<18)):
	print("No puedes pasar")
else:
	print("Puedes pasar")
print("")


print("Verificación de calificaciones")

nota_alumno=int(input("Introduce la nota del alumno por favor: "))