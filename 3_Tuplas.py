#las tuplas se escriben en parentesis () y las listas en []

mitupla=("Juan", 13,1,1995,13,13)
otratupla= "pedro", 12,4,78  #es una tupla pero se conoce como tupla empaquetada 


milista=list(mitupla) #metodo list para convertir una tupla en una lista
mitupla1=tuple(milista)  # el metodo tuple convertimos una lista en una tupla
mitupla2=("Carlos", 3,7,1984)
nombre, dia, mes, anio=mitupla2  #desempaquetado de una tupla 
#lo que hace es que asigna a cada varible un valor de la tupla en este caso mitupla2

#las tuplas tienen metodos como 
# in para saber si un elemento esta en una tupla
# count para contar so saber cuentos elementos tiene la tupla ó 
# count("Juan") nos devuleve cuantas veces tenemos este elemento en la tupla
# len nos devuelve el numero de elementos que tiene la tupla 

mituplaUnitaria=("Andres",)
print (len(mituplaUnitaria))
print(nombre)
print(dia)
print(mes)
print(anio)

print("imprimiendo una lista")
print(milista)
print(len(mitupla))
print(mitupla2)
