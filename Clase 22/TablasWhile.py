def run (): 
    print ("Hola, Bienvenido al programa de las Tablas Changuito Inc.")
    Tde = int(input ("De que número quieres ver la tabla: "))
    LIMITE = int(input("Hasta que número lo quieres multiplicar: "))
    contador = 0
    tm = Tde * contador
    
    while contador <= LIMITE:
         
        print (str(Tde)+" X " + str(contador)+" = "+str(tm))
        contador = contador + 1
        tm = Tde * contador


if __name__ == '__main__':
    run()



