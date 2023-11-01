#creamos una función para crear una lista con numero inicial y multiplicado por dos 

def generaPares (limite):
    num=1

    miLista=[]
    while num<limite:
        miLista.append(num*2)
        num= num+1
    
    return miLista

print(generaPares(10))

#creado por un generadr 
def generaPar(limite):
    num=1

    while num<limite:
        yield num*2
        num= num+1
    
devuelvePares=generaPar(10)

#for i in devuelvePares:
 #   print(i)

print(" imprimienso con metodo next")

print(next(devuelvePares))

print("Aqui tenemos más codigo")
print(next(devuelvePares))
print(" imprimienso con metodo next")
print(next(devuelvePares))