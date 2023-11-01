print("Programa de evaluacion de notas de alumnos")

# lo que introducimos por input siempre lo tomara como un string 
nota_alumno=input("Introduce la nota del alumno: ")

#python maneja el ambito de las variables 
def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
	return valoracion

# debemos hacer un casting con int para transformar como entero lo que pasamos por el input
print(evaluacion(int(nota_alumno)))
