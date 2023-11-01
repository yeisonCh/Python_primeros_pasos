import pickle

class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        
        print("se ha creado una nueva persona con el nombre: ", self.nombre)

    

#metodo str lo que hace es combertir en cadena de texto un objeto
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self. edad)
    
class listaPersonas:
    personas=[]

    def __init__(self):
        listaDePersonas=open("ficheroExterno","ab+")
        listaDePersonas.seek(0)
        try:
            self.personas=pickle.load(listaDePersonas)
            print("se cargaron {} personas del fichero externo ".format(len(self.personas)))
        except:
            print("el fichero está vacío")

        finally:
            listaDePersonas.close()
            del(listaDePersonas)


    def agregarPersonas(self,p):
        self.personas.append(p)

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)
    
    def guaradarPersonasEnFicheroexterno(self):
        listaDePersonas=open("ficheroExterno", "wb")
        pickle.dump(self.personas,listaDePersonas)
        listaDePersonas.close()

        del(listaDePersonas)

    def mostrarInformacionFicheroExterno(self):
        print("La información del fichero externo es la siguiente: ")
        for p in self.personas:
            print(p)

miListaPersonas=listaPersonas()


p=Persona("Pilar", "Femenino", 30)
miListaPersonas.agregarPersonas(p)

miListaPersonas.mostrarInformacionFicheroExterno()
