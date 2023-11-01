#practica condicional con if y else
edad=-7


#concatenación de comparadores 
# evalua condiciones de izquirda a derecha si se cumplen las dos condiciones ingresa en el if de lo contrario entra al else
if 0<edad<100:
	print("Edad es correcta")
else:
	print("Edad incorrecta")
print("------------------- Fin del primer programa--------------------------")


#practica condicional con if y else y concatenacion de operadores.
# se utiliza el int para hacer el casting de lo que recibimos por consola 
salario_presidente=int(input("Introduce el salario presidente: "))

#python no puede concatener dos tipos de datos diferentes 
#para eso utilizamos la funcion str que nos combierte un int en un string
print("Salario presidente: " + str(salario_presidente))

salario_director=int(input("Introduce el salario director: "))
print("Salario director: " + str(salario_director))

salario_jefe=int(input("Introduce el salario jefe de area: "))
print("Salario jefe: " + str(salario_jefe))

salario_administrativo=int(input("Introduce el salario administrativo: "))
print("Salario administrativo: " + str(salario_administrativo))


# python conpra por parejas las condiciones de izquierda a derecha
# si una de las parejas de condición falla salta de una vez al else sin ealuar las demas condiciones
if salario_administrativo<salario_jefe<salario_director<salario_presidente:
	print("Todo funciona correctamente")
else:
	print("Algo falla en esta empresa")
print("-------------Fin segundo programa ----------------------------")




