#practica condicional con if y else, concatenacion de operadores de comparacion y 
#uso de los operadores logicos and y or.
#programa para evaluiar tres condiciones 

print("Programa de becas año 2017")
distancia_escuela=int(input("Introduce la distancia a la escuela en kilometros: "))
print(distancia_escuela)
numero_hermanos=int(input("Introduce el numero de hermanos del aspirante: "))
print(numero_hermanos)
salario_familiar=int(input("Introduce el salario anual bruto de la familia: "))
print(salario_familiar)


#evaluara las condiciones en este la primera se debe cumplir y las dos siguientes se puede cumplir una de las dos
if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
	print("Tienes derecho a beca")
else:
	print("No tienes dercho a beca")
print("")