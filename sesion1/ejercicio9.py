''' 
*********** Curso de programación acelerada en Python ************ 
Date xx-xx-xxxx 
File: sesion/ejercicio9.py 
Autor: Programador x 
Action: salario mensual de un trabajador 
''' 
horas = float(input("Introduce tus horas diarias de trabajo: ")) 
coste = float(input("Introduce lo que cobras por hora: ")) 
salario_diario = horas * coste
salario_mensual = salario_diario * 30
print(f"Tu salario mensual es de : ", salario_mensual)