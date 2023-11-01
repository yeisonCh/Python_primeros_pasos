
#extructuras de datos pero estas se crean con asociandolas a una clave 
#clave: valor
#los dicionarios solo permiten tener claves unicas
midiccionario={"Alemania":"Berlin", "Francia":"Paris", "Reino Unido":"Londres", "España":"Madrid"}

#para acceder a una posicion del diccionario ponemos a imprimir el nombre de la clave 
print(midiccionario["Alemania"])

#para agrepar un nuevo elemento al diccionario 
midiccionario["Italia"]="Lisboa"

#para acceder a todo el diccionario
print(midiccionario)

#para modificar un elemento de un diccionario
midiccionario["Italia"]="Roma"
print(midiccionario)

#para eliminar un elemento a un diccionario
del midiccionario["Reino Unido"]
print(midiccionario)

midiccionario1={"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3}
print(midiccionario1)

#se puede crear una tipla y luego utilizarla con los elementos para crear un diccionario
mitupla=["Colombia", "Argentina", "Brasil", "Venezuela"]

#tomamos los valores de la tupla y creamos un diccionario agregandole valor 
midiccionario2={mitupla[0]:"Bogota", mitupla[1]:"Buenos Aires", mitupla[2]:"Brasilia", mitupla[3]:"Caracas"}
print(midiccionario2)
print(midiccionario2["Colombia"])

#podemos crear una tupla dentro de un diccionario
midiccionario3={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario3)

print(midiccionario3["Anillos"])
# para imprimir las claves de un diccionario
print(midiccionario3.keys())

#para imprimir los valores de un diccionario
print(midiccionario3.values())

#para imprimir  la cantidad de elementos de un diccionario
print(len(midiccionario3))