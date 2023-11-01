"""
import funciones_matematicas #importamos el modulo que hemos realizado anteriormente

op=funciones_matematicas

funciones_matematicas.sumar(2,5)
funciones_matematicas.restar(4,8)

op.multiplicar(4,8)
"""

from funciones_matematicas import sumar # podemos importar solamente las funciones que nec esitemos 

from funciones_matematicas import * #con el asterisco importamos todas las funciones que tenemos en el modulo

sumar(6,8)

multiplicar(4,9)

