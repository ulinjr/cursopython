''' 
*********** Curso de programación acelerada en Python ************ 
Date xx-xx-xxxx 
File: sesion/ejercicio7.py 
Autor: Programador x 
Action: imprime capital obtenido de una inversión 
''' 
cantidad = int(input("¿Cantidad a invertir? : ")) 
interes = float(input("¿Interés porcentual anual? : ")) 
años = int(input("¿Años? : ")) 
print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))