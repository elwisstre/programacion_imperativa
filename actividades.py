""" 
Se está realizando una encuesta sobre las actividades que realizan las personas
en su tiempo libre. A cada persona se le pregunta el tiempo libre que tiene semanalmente y la actividad principal
que realiza. Usted debe desarrollar un programa que permita registrar los datos de la encuesta. Para ingresar
los datos de cada persona se utilizan los siguientes códigos:

Tenga en cuenta que el programa debe permitir registrar la información de n personas, donde n es un número
entero digitado por el usuario. Una vez se termine de ingresar la información, debe aparecer la siguiente
información estadística:
• La cantidad de personas que tienen entre 6 y 9 horas libres y que prefieren leer.
• El porcentaje de personas que prefieren ver televisión en su tiempo libre

mayuscula, pedir correcto
"""

def encuesta():
    n = int(input("Ingrese la cantidad de encuestados: "))
    menos_6 = 0
    entre_6_9 = 0
    mas_9 = 0

    leer = 0
    television = 0
    deporte = 0
    dormir = 0

    porcentaje = television / n


    for i in range(0,n,1):
        tiempo_libre = int(input("¿Cuánto tiempo libre tienes? \nMenos de 6 horas: 1 \nEntre 6 y 9 horas: 2 \nMás de 9 horas: 3 \n"))
        actividad = input("¿Qué haces en tu tiempo libre? \nLeer: L \nVer televisión: TV \nHacer deporte: DP \nDormir: D \n")

        #CONVERSIÓN
        actividades = actividad.upper()

        #TIEMPO LIBRE OPCIONES
        if tiempo_libre == 1:
            menos_6 += 1
        elif tiempo_libre == 2:
            entre_6_9 += 1
        elif tiempo_libre == 3:
            mas_9 += 1
        else:
            print("Ingrese un valor válido.")

        #ACTIVIDAD OPCIONES
        if actividades == "L":
            leer += 1
        elif actividades == "TV":
            television += 1
        elif actividades == "DP":
            deporte += 1
        elif actividades == "D":
            dormir += 1
        else:
            print("Ingrese un valor válido.")


    print("La cantidad de personas que tienen entre 6 y 9 horas libres y que prefieren leer:")
    print("El porcentaje de personas que prefieren ver televisión en su tiempo libre:",porcentaje)






encuesta()
