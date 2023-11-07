from tkinter import *


raiz = Tk()

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

miNombre=StringVar()


labelNombre= Label(miFrame, text="Nombre: ")# pertenece al frame 
#nombreLabel.place(x=50, y=100)
labelNombre.grid(row=0,column=0, sticky="e", padx=10, pady=10) # el metodo grid adapta la venta al contenido de los lbel y los entry(cuadros de texto)

labelApellido= Label(miFrame, text="Apellido: ")# pertenece al frame 
labelApellido.grid(row=1, column=0, sticky="e", padx=10, pady=10)

labelPassword= Label(miFrame, text="Password: ")# pertenece al frame 
labelPassword.grid(row=2,column=0, sticky="e", padx=10, pady=10)

labeldireccion= Label(miFrame, text="Direccion: ")# pertenece al frame 
labeldireccion.grid(row=3,column=0, sticky="e", padx=10, pady=10)

labelComentarios= Label(miFrame, text="Comentario: ")# pertenece al frame 
labelComentarios.grid(row=4,column=0, sticky="e", padx=10, pady=10)






cuadroNombre=Entry(miFrame, textvariable=miNombre)
#cuadroTexto.place(x=100, y=100)
cuadroNombre.grid(row=0,column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="center")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1,column=1, padx=10, pady=10)

cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=2,column=1, padx=10, pady=10)
cuadroPassword.config(show="*")

cuadroComentario=Text(miFrame, width=16, height=5)
cuadroComentario.grid(row=4,column=1, padx=10, pady=10)

#contruir un scrollbar
scrollVert= Scrollbar(miFrame, command=cuadroComentario.yview)
scrollVert.grid(row=4,column=2, sticky="nsew")
cuadroComentario.config(yscrollcommand=scrollVert.set)


def codigoBoton():
    miNombre.set("Andres")


#crear botones 
botonEnviar=Button(raiz, text="Enviar", command=codigoBoton)
botonEnviar.pack()

 





raiz.mainloop()