"""Usted debe desarrollar un programa en Python que permita calcular el total a pagar por
una persona por concepto de entradas en un teatro. Para el ingreso se solicita la cantidad de adultos y de niños
que van a ingresar. Una boleta para adultos cuesta $12000 y para niños $8000. Además, el teatro tiene una
oferta del día que consiste en descontar el 17% del valor a pagar si ingresan al tiempo 2 o más adultos y 3 o
más niños. El programa muestra dos datos, el valor a pagar y si obtuvo, o no, la oferta día. """

def oferta_dia():
    adultos = int(input("Ingrese la cantidad de adultos: "))
    niños = int(input("Ingrese la cantidad de niños: "))
    valor_adulto = adultos * 12000
    valor_niño = niños * 8000
    
    if adultos >= 2 and niños >= 3:
        valor_total = valor_niño + valor_adulto 
        boletas = valor_total - (valor_total * 0.17)
        print(boletas)
        print("Usó la oferta del día!!!")
    else:
        boletas = valor_adulto + valor_niño
        print(boletas)

oferta_dia()


