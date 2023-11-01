#practica condicional con if y else y uso del operador in.
print("Asignaturas optativas año 2017")
print("Asignaturas optativas: informatica grafica - pruebas de software - usabilidad y accesibilidad")
opcion=input("Escribe la asignatura escogida: ")

# python es CASE SENSITIVE (distigue entre mayusculas y minusculas)
#usamos el metodo lower para pasar un string a minuscuas
# upper pasa un texto a mayusculas
asignatura=opcion.lower() 


# con el uso del operador in lo podemos usar para evaluar si un elementp se encuentra 
if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
	print("Asignatura elegida: " + asignatura)
else:
	print("La asignatura escogida no esta contemplada")