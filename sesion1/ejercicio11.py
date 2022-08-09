''' 
*********** Curso de programación acelerada en Python ************ 
Date 04-08-2022 
File: sesion2/ejercicio11.py 
Autor: .............. 
Action: detecta numero positivos, negativos y cero 
''' 
numero = int(input("Escriba un número : ")) 
if numero < 0: 
   print(f"El número ingresado {numero} es: NEGATIVO")
elif numero > 0: 
   print(f"El número ingresado {numero} es: POSITIVO")
else:
   print(f"El número ingresado {numero} es: CERO")
