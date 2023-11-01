import tkinter as tk

ventana = tk.Tk()
ventana.title("Ventana con ícono")
ventana.geometry("300x200")
ventana.iconbitmap("D:/Documents/Ejercicios/Graficos/icon.ico")

miFrame= Frame()
miFrame.pack() #empaquetar el frame

ventana.mainloop()