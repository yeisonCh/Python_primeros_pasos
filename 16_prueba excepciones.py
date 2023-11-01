def divide():
    try:
        op1= (float(input("intruduce primer número")))
        op2 = (float(input("intruduce segundo número")))
        print ("division es: " + str(op1/op2))

    except ValueError:

        print("El valor introducido es erroneo ")
    
    except ZeroDivisionError:

        print ("No se puede dividir entre cero")

    print("Calculo finalizado")

    divide()
