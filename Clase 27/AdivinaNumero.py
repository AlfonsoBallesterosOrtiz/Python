import random

def run ():
    numeroaleatorio = random.randint(1,100)

    # numeroaleatorio = 1

    numeroelegido = int (input ("Elige un número entre 1 y 100: "))
 
    while numeroelegido != numeroaleatorio:
        if numeroelegido < numeroaleatorio:
            print ("Fallaste chango, piensa en grande, sin miedo al éxito")
                
        else :
            print ("Te pasaste de galleta, piensa un número más pequeño")
            
        numeroelegido = int (input ("Piensa en otro número: "))
            
    print ("Felicidades, has ganado")        

if __name__ == "__main__":
    run ()


