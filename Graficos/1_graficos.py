from tkinter import *

raiz=Tk()
raiz.title("ventana de pruebas")
#aiz.resizable(1,1)# dos parametros bolena 0=false 1=true  el primero width el segundo  height
raiz.iconbitmap("D:/Documents/Ejercicios/Graficos/icon.ico") #cambiar el icono de una ventana
#raiz.geometry("650x450") #tamaño de la ventana
raiz.config(bg="blue")

miFrame= Frame()
miFrame.pack() #empaquetar el frame fijamos el contenedor o el frame 
miFrame.config(bg="red")
miFrame.config(width="650", height="400")




raiz.mainloop() 
# el metodo mainloop() es un bucle infinit