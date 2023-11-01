 #se utiliza el * antes del argumento
#se usa para indicar que se va recibir más de un elemnto en una tupla


def devulebeCiudades(*ciudades):
    for elemento in ciudades:
        #for sub in elemento:
          #  yield sub
        yield from elemento   #para mostrar los subelementos de las ciudades en este caso las letras

    


ciudadesDevueltas = devulebeCiudades("Madrid","Barcelona","Bilbo","Valencia")

print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))