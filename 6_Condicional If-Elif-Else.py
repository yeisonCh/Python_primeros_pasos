print("Verificación de acceso")

edad_usuario=int(input("Introduce tu edad por favor: "))

if edad_usuario<18:
	print("No puedes pasar")
elif edad_usuario>100:
	print("Edad incorrecta")
else:
	print("Puedes pasar")
print("")


print("Verificación de calificaciones")

nota_alumno=int(input("Introduce la nota del alumno por favor: "))

if nota_alumno<5:
	print("Insuficiente")
elif nota_alumno<6:
	print("Suficiente")
elif nota_alumno<7:
	print("Bien")
elif nota_alumno<9:
	print("Sobresaliente")	
else:
	print("Excelente")
print("")
print("El programa ha finalizado")