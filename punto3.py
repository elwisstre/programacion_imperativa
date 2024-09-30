"""Una Constructora ofrece casas de interés social, bajo las 
siguientes condiciones: Si los ingresos del comprador son 
menores de $3.000.000, la cuota inicial será del 20% del 
costo de la casa y el resto de la deuda se le aplica un interés 
del 15% y se distribuye en pagos mensuales, a pagar en diez 
años.  
Si los ingresos del comprador son desde $3.000.000, la cuota inicial será del 30% del costo de la 
casa y el resto de la deuda se le aplica un interés del 18% y se distribuirá en pagos mensuales a 
pagar en 7 años. 
La empresa quiere que los estudiantes de primer semestre de programación imperativa realicen un 
programa en Python, que lea la información de n interesados en comprar casa.  Por cada interesado 
se debe pedir el nombre, el ingreso mensual, y el valor de la casa que desea comprar.  y a partir de 
ella calcule y muestre el valor que debe pagar de la cuota inicial, el valor que van a pagar por 
intereses, el porcentaje del interés,  el saldo de la deuda y el valor de la cuota que debe pagar y la 
cantidad de cuotas a pagar.  
Cuando se termine el ingreso de los n interesados (donde n es un número ingresado por el usuario) 
se debe imprimir la cantidad de personas con ingresos menores a 3.000.000 que consultaron, y el 
nombre y el sueldo de las personas que consultaron con ingresos desde 3.000.000"""

def compra():
    n = int(input("digite el numero de interesados: "))
    menores3 = ""
    mayores3 = ""
    



    for i in range(1,n+1,1):
        nom = input("porfavor digite su nombre: ")
        ing = float(input("digite el total de sus ingresos mensuales: "))
        val = float(input("ingrese el valor de la casa que desea adquirir: "))
        if ing < 3000000:
            total_casa1 = 0.20 * val
            totaliti = val - total_casa1
            quince = totaliti * 0.15
            diezaños1 = (totaliti + quince)
            dividido = (totaliti + quince) / 120
            menores3 = menores3 + "personas con sueldos menores a 3m" "\n" "nombre: " + nom + "\n" "ingresos mensuales: " + str(ing) + "\n"
            print("el valor de la cuota inicial basado en sus ingresos mensuales es:", total_casa1)
            print("los intereses a pagar son de:", quince)
            print("el saldo restante es de: ", diezaños1)
            print("el valor a pagar mensual durante diez años es de: ", dividido)


            """A 10 años el ultimos"""


        elif ing >= 3000000:
            total_casa2 = 0.30 * val
            totaliti2 = val - total_casa2
            diezyocho = totaliti2 * 0.18
            sieteaños2 = (totaliti2 + diezyocho)
            dividio2 = (totaliti2 + diezyocho) / 84
            mayores3 = mayores3 +"peronas con sueldos mayores o iguales a 3m" "\n" "nombre: " + nom + "\n" "ingresos mensuales: " + str(ing) + "\n"
            print("el valor de la cuota inicial basado en sus ingresos mensuales es:", total_casa2)
            print("los intereses a pagar son de:", diezyocho)
            print("el saldo restante es de: ", sieteaños2)
            print("el valor a pagar mensual durante diez años es de: ", dividio2)

            """A 7 años el ultimo"""

    print(mayores3)
    print(menores3)
    
compra()
