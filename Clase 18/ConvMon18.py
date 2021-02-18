def conversor (tipo_pesos, valor_dolar):
    pesos = input("Ingrese el total de pesos " + tipo_pesos +" a convertir: $ ")
    pesos = float (pesos)
    USD = pesos / valor_dolar
    USD = round (USD,2)
    USD = str(USD)
    print ("Tienes un total de: $ " + USD + " dólares")


menu = """
Bienvenido al Conversor de Monedas de Changuito Inc. 🐵
1.- Pesos colombianos
2.- Pesos argentinos
3-- Pesos mexicanos

Elige una opción: """
opcion = input (menu)
opcion = int(opcion)

if opcion == 1:    
    conversor ("colombianos", 3875)

elif opcion == 2:
    conversor("argentinos", 87.90)

elif opcion == 3:   
    conversor("mexicanos", 20.44)
else:
     print ("Ingrese una opción del menú, no sea chango.  Gracias")

