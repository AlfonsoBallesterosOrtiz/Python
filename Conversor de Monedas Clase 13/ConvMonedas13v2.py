USD = input("Ingrese el total de dólares (USD) a convertir: $ ")
USD = float (USD)
MXNV = 1/19.80
MXN = USD / MXNV
MXN = round (MXN,2)
MXN = str(MXN)
print ("Tienes un total de: $ " + MXN + " pesos mexicanos")