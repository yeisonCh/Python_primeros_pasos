from tkinter import *

root=Tk()
"""
raiz.title("ventana de pruebas")
#aiz.resizable(1,1)# dos parametros bolena 0=false 1=true  el primero width el segundo  height
raiz.iconbitmap("D:/Documents/Ejercicios/Graficos/icon.ico") #cambiar el icono de una ventana
#raiz.geometry("650x450") #tamaño de la ventana
raiz.config(bg="blue")
"""

miFrame=Frame(root, width=500, height=400)
miFrame.pack() #empaquetar el frame fijamos el contenedor o el frame 

"""
miLabel= Label(miFrame, text="Hola compañeros de python esta es una prueba") # primer parametro el contenedor padre 
miLabel.place(x=100, y=60)# empaquetamos el label 

"""
miImagen= PhotoImage(file="D:/Documents/Ejercicios/Graficos/Captura.png")
#lo podemos abrebiar con 
Label(miFrame, text="Hola a todos esta es otra prueba", fg="red", font=("Comic Sans MS", 14)). place(x=100, y=70)
Label(root, image=miImagen).place(x=100, y=200)




root.mainloop() 
# el metodo mainloop() es un bucle infinit