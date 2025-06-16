import os, time

entradas =[]

def venta_entradas():
    nombre=input("Nombre del comprador: ")
    if nombre in entradas:
        print("el comprador Ya tiene su entrada.")
        return
    tp_entrada = input("tipo de entrada (G o V)")
    cdg = input("configuracion de codigo()")

    entrada= {
        "comprador": nombre,
        "entrada": tp_entrada,
        "codigo": cdg
    }
    entradas.append(entrada)
    print("Entrada comprada con éxito.")
    time.sleep(3)
    os.system('cls')

def consultar_comprador(entradas):
    print("consultar comprador")
    nombre =input("ingrese nombre de comprador: ")
    encontrado=False
    for entrada in entradas:
        
