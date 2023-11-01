import math 


def calculaRaiz (num1):
    if num1<0:
        raise ValueError("El número no puede ser negativo")
    
    else:
        return math.sqrt(num1)

op1=(int(input("introduce un número..  ")))

try:
    print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)
print("programa terminado")



def evaluaEdad(edad):

    if edad <0:
        raise TypeError("No se permiten eades negativas") # raise  nos perite lanzar una ecepción 
    if edad<20:
        return "eres muy joven"
    elif edad <40:
        return "Eres Joven"
    elif edad <65:
        return "eres maduro"
    elif edad <100:
        return"cuidate.."
    

print(evaluaEdad(14))
    
