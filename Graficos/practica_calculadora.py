from tkinter import *

raiz= Tk()
# frame 
miFrame= Frame(raiz)

miFrame.pack()

operacion=""
resultado=0

#------------------- pantalla  -------------------------
numeroPantalla= StringVar() #variable para capturar el numero o el boton que pulsamos
pantalla = Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right",)

#--------------- pulsaciones teclado ----------------------
def numPulsado(num):
    
    global operacion

    if operacion!="":
        numeroPantalla.set(num)
        operacion=""
    else:
        numeroPantalla.set(numeroPantalla.get() + num)


# ------------- funcion suma --------------------
def suma(num):
    global operacion
    global resultado

    resultado+= int(num)
    operacion = "suma"
    numeroPantalla.set(resultado)

# ----- funcion resultado -------------------------------

def el_resultado():
    global resultado

    numeroPantalla.set(resultado +int(numeroPantalla.get()))
    resultado=0

#--- fial de botonos 7,8,9 y el boton multiplicar --------

boton7= Button(miFrame, text="7", width=3, command=lambda:numPulsado("7"))
boton7.grid(row=2, column=1)
boton8= Button(miFrame, text="8", width=3, command=lambda:numPulsado("8"))
boton8.grid(row=2, column=2)
boton9= Button(miFrame, text="9", width=3, command=lambda:numPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv= Button(miFrame, text="/", width=3)
botonDiv.grid(row=2, column=4)


#--- fial de botonos 4,5,6 y el boton multiplicar --------

boton4= Button(miFrame, text="4", width=3, command=lambda:numPulsado("4"))
boton4.grid(row=3, column=1)
boton5= Button(miFrame, text="5", width=3, command=lambda:numPulsado("5"))
boton5.grid(row=3, column=2)
boton6= Button(miFrame, text="6", width=3, command=lambda:numPulsado("6"))
boton6.grid(row=3, column=3)
botonMul= Button(miFrame, text="*", width=3)
botonMul.grid(row=3, column=4)


#--- fial de botonos 1,2,3 y el boton multiplicar --------

boton1= Button(miFrame, text="1", width=3, command=lambda:numPulsado("1"))
boton1.grid(row=4, column=1)
boton2= Button(miFrame, text="2", width=3, command=lambda:numPulsado("2"))
boton2.grid(row=4, column=2)
boton3= Button(miFrame, text="3", width=3, command=lambda:numPulsado("3"))
boton3.grid(row=4, column=3)
botonRes= Button(miFrame, text="-", width=3)
botonRes.grid(row=4, column=4)


#--- fial de botonos 0,8,9 y el boton multiplicar --------

boton0= Button(miFrame, text="0", width=3, command=lambda:numPulsado("0"))
boton0.grid(row=5, column=1)
botonComa= Button(miFrame, text=",", width=3)
botonComa.grid(row=5, column=2)
botonIgual= Button(miFrame, text="=", width=3, command=lambda:el_resultado())
botonIgual.grid(row=5, column=3)
botonSum= Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5, column=4)



raiz.mainloop()