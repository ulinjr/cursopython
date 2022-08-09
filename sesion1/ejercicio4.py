''' 
*********** Curso de programación acelerada en Python ************ 
Date xx-xx-xxxx 
File: sesion/ejercicio4.py 
Autor: Programador x 
Action: pago de trabajador 
''' 
horas = float(input("Introduce tus horas de trabajo: ")) 
coste = float(input("Introduce lo que cobras por hora: ")) 
horas_extras = float(input("Ingresa el número de horas extras : "))
pago_extra = horas_extras * coste
paga = (horas * coste) + pago_extra 
print("Tu paga es", paga)