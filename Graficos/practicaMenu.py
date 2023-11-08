from tkinter import *
from tkinter import messagebox #para ventanas emergentes

root= Tk()
def infoAdicional():
    messagebox.showinfo("Procesador de Andres", "procesador de textos 2018")

def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia generica")

def salirAplicacion():
   #valor=messagebox.askquestion("Salir","Deseas salir de la palicación?")
    valor=messagebox.askokcancel("Salir","Deseas salir de la palicación?")

    #if valor=="yes": para askquestion
    if valor=="true": # para askokcancel
        root.destroy()


def cerrarDocumento():
    valor=messagebox.askretrycancel("Reintentar","No es posible cerrar, Documento bloqueado?")
    if valor=="false": # para askokcancel
        root.destroy()


barraMenu= Menu(root)
root.config(menu=barraMenu, width=400, height=400)

#establecmos la cantidad de elementos tiene el menu

archivoMenu=Menu(barraMenu, tearoff=0) #tearoff=0 para quitar la linia que sale al inicio del menu
#sub elementos 
archivoMenu.add_command(label="Nuevos")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
#crear barra de ceparación 
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

archivoEdecion=Menu(barraMenu, tearoff=0)
archivoEdecion.add_command(label="Copiar")
archivoEdecion.add_command(label="Cortar")
archivoEdecion.add_command(label="Pegar")
archivoEdecion.add_command(label="remplazar")


archivoHerramientas=Menu(barraMenu,tearoff=0)


archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdecion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

#agregamos sub elementos 


root.mainloop()