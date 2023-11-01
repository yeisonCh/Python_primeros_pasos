from io import open


archivo_texto=open("archivo.txt", "r+") #si el segundo parametro lo especificamos como r+ 
#nos habre e archivo en modo lectura y escritura


#archivo_texto.seek(11)
print(archivo_texto.read())
archivo_texto.seek(len(archivo_texto.read())/2)


print("---------------------------")
print(archivo_texto.read())

archivo_texto.write("\n agregando más texto al archivo de prueba")

print(archivo_texto.read())
archivo_texto.close()