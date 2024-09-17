"""
Desarrollar un programa que solicite la edad de tres usuarios y muestre un
mensaje indicando si es menor de edad, adulto o pertenece a la tercera edad
"""

"""
MODIFICACIÓN
Salida:
Mostrar al finalizar el ingreso de todos los usuarios un listado con el nombre,
la edad y la etapa de la vida.
Mostrar la cantidad de usuarios mayores a 80 años.
El porcentaje de usuarios menores de edad.
El promedio de edades de los adultos.
Muestre la cantidad de usuarios que en su nombre tengan más de 2 vocales
Al finalizar muestre las personas que el nombre inicie en vocal y finalice en
n o s
"""
def etapaDeLaVida():
    lista_usu = ""
    cant_usu =int(input("Ingrese la cantidad de usuarios: "))
    mayores = 0
    menores = 0
    por_adulto = 0
    etapa = ""
    vocales = "aeiouAEIOU"

    


    for u in range(1,cant_usu+1,1):
        edad = int(input("Digite la edad del usuario"+str(u)+":"))
        nombre = input("Digite el nombre del usuario"+str(u)+":")

        while(edad < 1 or edad > 120):
            print("Edad incorrecta!")
            edad = int(input("Digite la edad del usuario"+str(u)+":"))

        if(edad >= 1 and edad < 18):
            etapa = "Es menor de edad"
            menores += 1
            por_menores = menores / cant_usu * 100

        elif (edad >= 18 and edad < 60):
            etapa = "Es adulto"
            por_adulto += 1
            promedio = por_adulto / cant_usu * 100

        elif(edad >= 60 and edad <= 120):
            etapa = "Es de la tercera edad"
            mayores += 1
            por_adulto += 1
            promedio = por_adulto / cant_usu * 100
        else:
            print("Ingrese una edad válida!")




        lista_usu = lista_usu + "Nombre:" + nombre +" Edad:" + str(edad) + " Etapa:" + etapa + "\n"

        cant_vocal = nombre.count("a","e","i","o","u","A","E","I","O","U")






    print(lista_usu)
        
    print("La cantidad de encuestados mayores es:",mayores)
    print("El porcentaje de encuestados menores es:",por_menores,"%")
    print("El porcentaje de adultos es:",promedio,"%")
    print("La cantidad de encuestado que tiene vocales en su nombre es:", cant_vocal)


etapaDeLaVida()
        
