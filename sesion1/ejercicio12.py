''' 
*********** Curso de programación acelerada en Python ************ 
Date 04-08-2022 
File: sesion2/ejercicio12.py 
Autor: .............. 
Action: valida si el usuario es correcto 
''' 
PALABRA_CLAVE = "python"
nombre_usuario = input("Ingrese su nombre de usuario : ") 
password = input("Ingrese contarseña : ")
if password != PALABRA_CLAVE: 
   print(f"ERROR...Constraseña del usuario {nombre_usuario} : INVALIDA")
