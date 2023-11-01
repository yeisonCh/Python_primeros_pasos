import math
i=1

while i<=5:
    print("Ejecución " + str(i))
    i= i+1

print("Termin la ejecución del bucle while")

edad = int(input("escribe tu edad: "))

while edad<5 or edad>100:
    print("la edad es incorrecta")
    edad = int(input("escribe tu edad: "))

print ("La edad es correcta")

print ("Edad introducida " +str(edad))

print ("Programa para hallar la raiz cuadrada")

numero= int(input("Introduce un numero: "))

intentos=0

while numero<0:
    print("No se puede hallar la raiz de un numero negativo")

    if intentos ==2:
        print("solo tenias dos intentos =(")
        break; #detiene el flujo del programa o del ciclo
    numero= int(input("Introduce un numero: "))
    if numero<0:
        intentos =intentos+1
if intentos<2:
    solución=math.sqrt(numero)
    print("la raiz cuadrada es "+ str(numero) + " es " + str(solución))