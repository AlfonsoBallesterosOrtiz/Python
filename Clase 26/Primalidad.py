def es_primo (b):
    contador = 0

    for i in range (1,b+1):
        if i == 1 or i == b:
            continue
        if b % i == 0:
            contador +=1
    
    if contador == 0:
        return True
    else:
        return False


def run ():
    a = int (input ("Quieres saber si un numero es un numero primo? Captura 1=Si , 2=Me vale: "))
    if a == 2:
        print ("Chinga tu madre")
    if a == 1:
        b = int (input ("Captura un numero: "))
        if es_primo(b) == True:
            print ('Es primo')
        else:
            print ('No es primo')
    if a > 2:
        print ("Que eres pendejo y no distingues entre 1 y el 2?")

if __name__ == "__main__":
    run ()
