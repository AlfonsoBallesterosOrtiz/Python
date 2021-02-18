def suma (a, b):
    print ("El resultado de la suma es: ")
    resultado = a + b
    return resultado

a = input ("Capture primer valor: ")
a = int (a)
a = float (a)

b = input ("Capture segundo valor: ")
b = int (b)
b = float (b)


sumatoria = suma(a, b)
print (sumatoria)
