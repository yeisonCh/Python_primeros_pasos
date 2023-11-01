#creando clases en python y a partir de estas podemos crer instancias de clases o objetos

class Coche():
    #creamos el metodo constructor para Coche
    def __init__(self):  #con dos guiones bajos
        self.__largoChasis=250    #propiedades 
        self.__anchoChasis=120  # para encapsular una variable ruedas anteponemos dos guiones bajos
        self.__ruedas=4
        self.__enMarcha=False

#creando comportamientos o métodos de la clase

    def Arrancar(self,arrancamos):
        self.__enMarcha=arrancamos #esto evalua si esta en true o en false 
        if(self.__enMarcha):
            chequeo=self.__chequeoInterno()

        if (self.__enMarcha and chequeo):
            return "el coche esta en marcha "
        elif (self.__enMarcha and chequeo==False):
            return "algo esta mal en el chequeo"
        else: 
            return "El coche esta parado "

    
    def estado(self):
        print("el coche tinen ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis )

#encapsular metodo, lo hacemos utilizando dos guiones bajos 
    def __chequeoInterno(self):
        print("realizando chequeo interno")

        self.gasolina= "ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

#construimos objetos con la clase que hemos creado o instanciación de clase 

miCoche = Coche()

print(miCoche.Arrancar(True))
miCoche.estado()


print(" ")
print("-----  segundo objeto --------------")
print(" ")

miCoche2 =Coche()

print(miCoche2.Arrancar(False))
miCoche2.estado()