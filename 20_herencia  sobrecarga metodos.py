
# ----------- Clase veiculos -------------

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
              "\nFrenando: ", self.frena) #utilizamos \n para un salto de linea al verlo en consola


 # ----------- Clase Furgoneta --------------------
class Furgoneta(Vehiculos):
    def carga(self,cargar):
        self.cargado=cargar
        if(self.cargado):
            return "la furgoneta está cargada"
        else:
            return "la furgoneta no está cargada"
        

# --------------- Clase Motos ------------------------

#herencia de clase para ello en los parametros de la clase le pasamos la clase padre
class Moto(Vehiculos):
    hcaballito="--"

    def caballito(self):
        self.hcaballito= "voy haciendo el caballito"
    
    def estado (self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo,
              "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera,
              "\nFrenando: ", self.frena, "\n", self.hcaballito) #utilizamos \n para un salto de linea al verlo en consola
        
#--------------- clase vehiculos electrico ------------
class Velectricos():
    def __init__(self):
        self.autonomia=100
    
    def cargarEnergia(self):
        self.cargando=True

#----------- clase bicicleta electrica -----------------
class bicicletaElectrica(Velectricos, Vehiculos):
    pass

#---------- FIN CLASES --------------------------------

#---- Instancias de clases -----------------------

miMoto=Moto("Honda", "CBR")

#miMoto.caballito() 
miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Kongoo")

miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

#cuando tenemos herencia multiple se le da prioridad al constructor del primer parametro de la herencia 
# en este caso de Velectricos
miBici=bicicletaElectrica()

