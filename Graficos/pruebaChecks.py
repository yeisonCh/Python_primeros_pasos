from tkinter import *

root=Tk()
root.title("Ejemplo check")

playa= IntVar()
montagna=IntVar()
turismorural=IntVar()
def opcionesViaje():
    opcionEscogida=""

    if (playa.get()==1):
        opcionEscogida+=" playa"

    if (montagna.get()==1):
        opcionEscogida+=" montaña"

    if (turismorural.get()==1):
        opcionEscogida+=" turismoRural"
    
    etiqueta.config(text=opcionEscogida)


foto= PhotoImage(file="D:/Documents/Ejercicios/Graficos/avion.png")
Label(root, image=foto).pack()

frame=Frame(root).pack()

Label(frame, text="Elige destinos: ", width=50).pack()



Checkbutton(root, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="Montaña",variable=montagna, onvalue=1,offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="Turismo rural", variable=turismorural, onvalue=1,offvalue=0, command=opcionesViaje).pack()

etiqueta= Label(frame)
etiqueta.pack()

root.mainloop()