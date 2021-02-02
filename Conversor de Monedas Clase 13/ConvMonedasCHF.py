CHF = input("Ingrese el total de francos suizos (CHF) a convertir: $ ")
CHF = float (CHF)
CHFV = input("Ingrese el equivalente en pesos (MXN) de 1 CHF ")
CHFV = float (CHFV)
MXNV = 1/CHFV
MXN = CHF / MXNV
MXN = round (MXN,2)
MXN = str(MXN)
print ("Tienes un total de: $ " + MXN + " pesos mexicanos")