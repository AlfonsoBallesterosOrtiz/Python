def run ():
    print ("Bienvenido al programa de Tablas con el ciclo For de Changuito Inc.")
    a = int (input("¿De qué número quieres conocer la tabla?: "))
    b = int (input( "¿Hasta que número la quieres multiplicar?: "))

    c = range (1, b+1)

    for i in c:
        print ( str (a)+ " x " + str (i) + " = " +  str (a * i))

if __name__ == "__main__":
    run ()
