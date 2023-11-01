import pickle

lista_nombre=["Pedro", "Ana", "Maria", "Isabel"]

fichero_binario=open("lista_nombres","wb") #escritura binaria wb

#bolcamos la lista al fichero externo

pickle.dump(lista_nombre,fichero_binario)
#argumentos lista y el segundo fichero 

fichero_binario.close()

del(fichero_binario) #borrar de la memoria el fichero binario