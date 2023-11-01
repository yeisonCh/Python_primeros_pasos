from io import open

"""
#crear un documento 
archivo_texto=open("archivo.txt", "w")#dos argumentos (nombre, mode de abrrir)-> lectura(r), escritura(w) 
frase= "Hola a todos esta es una prueba de escritura desde python a un archivo txt"


#manipular el archivo
archivo_texto.write(frase)

#cerrar el  que se ha abierto en memoria desde python
archivo_texto.close()


PARA ABRIR EL ARCHIVO EN MODO LECTURA 

archivo_texto=open("archivo.txt", "r")

#texto=archivo_texto.read()  #tambien podemos utilizar el metodo readline

linias_texto=archivo_texto.readline() #para que el texto lo transforme en una lista
archivo_texto.close()
"""
archivo_texto=open("archivo.txt", "a") # a de apend 
archivo_texto.write("\n Siempre es una buena ocacion para estudiar python")
archivo_texto.close()



