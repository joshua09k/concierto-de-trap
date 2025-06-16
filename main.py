# Ejercicio Tipo Prueba 1:
import os, time
from Funciones import *
entradas = []

os.system('cls')
menu = """--- MENÚ PRINCIPAL 
1. Comprar Entrada.
2. Consultar Comprador.
3. Cancelar Compra.
4. Salir."""
print(menu)
while True:
    opc = int(input("ingrese opción: "))

    if opc == 1:
        venta_entradas()
    elif opc == 2:
        pass 
    elif opc == 3:
        pass
    elif opc == 4:
        print("cargando opción")
        break
    else:
        print("opción invalida")

     
