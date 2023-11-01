import pickle

fichero= open("lista_nombres", "rb") #permiso lectura binaria rb

lista=pickle.load(fichero)

print(lista)

