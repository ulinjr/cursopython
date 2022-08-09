''' 
*********** Curso de programación acelerada en Python ************ 
Date 04-08-2022 
File: sesion2/ejercicio20.py 
Autor: .............. 
Action: Genera tabla de multiplicar
''' 
n = int(input("Ingresa un número de tabla [1.10]: "))
print(f"Tabla de multiplicar del número : {n}")
for i in range(10):
  r = n * (i + 1) 
  print(f"{n} X {i+1} = {r}")