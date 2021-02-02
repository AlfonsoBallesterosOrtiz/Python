pesos = input("Ingrese el total de pesos (MXN) a convertir: $(MXN) ")
pesos = float (pesos)
CHFValor = input("Ingrese el equivalente en pesos (MXN) de 1 CHF ")
CHFValor = float (CHFValor)
CHF = pesos / CHFValor
CHF = round (CHF,2)
CHF = str(CHF)
print ("Tienes un total de: CHF " + CHF + " francos suizos")
