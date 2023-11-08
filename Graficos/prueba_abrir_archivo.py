from tkinter import *
from tkinter import filedialog

root= Tk()

def abrirFichero():
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Ficheros de Excel", "*.xlsx"),("Ficheros de texto","*.txt"),
                                                                                  ("Todos los ficheros","*.*"))) 
    #initialdir="C:"  el directorio donde quiero iniciar la busqueda

    print(fichero)


Button(root, text="Abrir fichero", command=abrirFichero).pack()

root.mainloop()