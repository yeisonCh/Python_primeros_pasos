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
# leer el archivo serializado 

ficheroApertura= open("losCoches", "rb")
misCoches= pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:
    print(c.estado())