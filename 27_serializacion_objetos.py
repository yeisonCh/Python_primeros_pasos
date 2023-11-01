import pickle #libreria para serializar

class Vehiculos():
    def __init__(self,marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    
    def arrancar (self):
        self.enmarcha=True
    
    def acelerar(self):
        self.acelera=True

    def frenat(self):
        self.frena=True

    def estado (self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo,
              "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera,
              "\nFrenando: ", self.frena) #utilizamos \n para un salto de linea 
        
coche1=Vehiculos("Mazda","MX5")
coche2=Vehiculos("Seat","Leon")
coche3=Vehiculos("Renault","Megane")
#creamos una coleccion con las instancias creadas 

coches=[coche1,coche2,coche3]
#Creamos una variable para serilizar el objeto

fichero=open ("losCoches", "wb")
pickle.dump(coches, fichero)

fichero.close()


del(fichero)

# leer el archivo serializado 

ficheroApertura= open("losCoches", "rb")
misCoches= pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:
    print(c.estado())