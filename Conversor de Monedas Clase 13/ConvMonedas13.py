pesos = input("Ingrese el total de pesos (MXN) a convertir: $(MXN) ")
pesos = float (pesos)
USDValor = 19.80
USD = pesos / USDValor
USD = round (USD,2)
USD = str(USD)
print ("Tienes un total de: $ " + USD + " dólares")
