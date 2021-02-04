menu = """
Bienvenido al Conversor de Monedas de Changuito Inc. 🐵
1.- Pesos Colombianos
2.- Pesos Argentinos
3-- Pesos Mexicanos

Elige una opción: """
opcion = input (menu)
opcion = int(opcion)
if opcion == 1:    
    pesosC = input("Ingrese el total de pesos colombianos a convertir: $(COL) ")
    pesosC = float (pesosC)
    USDValorC = 3557.00
    USDC = pesosC / USDValorC
    USDC = round (USDC,2)
    USDC = str(USDC)
    print ("Tienes un total de: $ " + USD + " dólares")

elif opcion == 2:
    pesosA = input("Ingrese el total de pesos argentinos a convertir: $(ARG) ")
    pesosA = float (pesosA)
    USDValorA = 87.90
    USDA = pesosA / USDValorA
    USDA = round (USDA,2)
    USDA = str(USDA)
    print ("Tienes un total de: $ " + USDA + " dólares")
elif opcion == 3:   
    pesosMx = input("Ingrese el total de pesos mexicanos a convertir: $(MXN) ")
    pesosMx = float (pesosMx)
    USDValorMx = 20.44
    USDMx = pesosMx / USDValorMx
    USDMx = round (USDMx,2)
    USDMx = str(USDMx)
    print ("Tienes un total de: $ " + USDMx + " dólares")
else:
     print ("Ingrese una opción del menú, no sea chango.  Gracias")

