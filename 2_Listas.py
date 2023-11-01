#listas 
#nos permite almacenar valires de diferentes tipos
# el simbolo * es un multiplicar o nos sirve para repetir el contenido de una lista
# est lista esta compuesta por un string, entero, bolean, float
milista=["Maria", 5, True, 78.35] * 3

#para imprimir toda la lista la sintaxis es milista[:]

# al insertar valores negativos cuando imprimimos o accedemos a una lista python inicia a contar desde el ultimo hacia adelante 
# tomando como el ultimo como posición -1

#para imprimir  acceder a un elemento de la lista milista[2]
print(milista[3])

#para acceder a una porción de la lista usamos milista[:3]
print(milista[1:4])
print("--------------------")
print(milista[:])

#agregar elementos al final de una lista 
milista.append("Sandra")
print("agregamos Sandra al final de la lista")
print(milista[:])
#para agregar a un punto intermedio nos solicita dos arumentos 
#la posición y el elemento a insertar 

print("Agregamos una joel en una posición determinada")
milista.insert(1,"Joel")
print(milista[:])

#agregamos varios elementos a una lista 
milista.extend(["pedro", "Julian"])
print(milista[:])

#validar posición en una lista 
print("Sandra esta en la posición #")
print(milista.index("Sandra"))


#para verificar si un elemento esta en una lista 
print("Felipe" in milista)


#eliminar elementos   milista.remove("Ana")
#eleiminar el ultimo elemento de una lista milista.pop()