def suma (num1,num2):
    return num1 + num2

def resta (num1,num2):
    return num1 - num2

def multiplica(num1,num2):
    return num1 *num2

def divide(num1,num2):
    try:
        return num1 /num2
    except ZeroDivisionError:
        print("NO SE PUEDE DIVIDIR ENTRE CERO")
        return "Operación erronea"

while True: 
    try:
        op1 = (int(input("Introduce primer número:  ")))
        op2 = (int(input("Introduce segundo número:  ")))
        break;
    except ValueError: 
        print("Los valores intruducidos no son correctos intruducelos denuevo")
operacion = (input("Introduce la operacin a realizar (Suma, resta, multiplica, divide)  "))

if operacion=="suma":
    print(suma(op1,op2))

elif operacion=="resta":
    print(resta(op1,op2))

elif operacion=="multiplica":
    print(multiplica(op1,op2))

elif operacion=="divide":
    print(divide(op1,op2))

else :
    print("operacion no contemplada")

print("Operacion ejecutada. continuacion de la ejecución del programa")