''' 
*********** Curso de programación acelerada en Python ************ 
Date 04-08-2022 
File: sesion2/ejercicio18.py 
Autor: .............. 
Action: suma valores ingresados por teclado
''' 
ITEMS = 3
suma = 0 
for f in range(ITEMS): 
  valor = int(input("Ingrese valor:")) 
  suma = suma + valor 
print("La suma es") 
print(suma) 
promedio = suma / ITEMS 
print("El promedio es:") 
print(promedio)