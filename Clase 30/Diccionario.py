def run ():
    print ("Bienvenido al diccionario Changuito")
    print ( 'Puedo dar la poblacion de estos cuatro paises: Suiza, Argentina, Brasil y Mexico')

    # mi_diccionario = {
    #     'llave1' : 1,
    #     'llave2' : 2,
    #     'llave3' : 3,
    # }

    # print (mi_diccionario ['llave1'])
    # print (mi_diccionario ['llave2'])
    # print (mi_diccionario ['llave3'])

    # a = input ('Que llave quiere imprimir?: ')

    # print (mi_diccionario [a])

    dicpaises = {

        'Suiza' : 8.57,
        'Argentina' : 44.49,
        'Brasil' : 209.5,
        'Mexico' : 126.2,
    }



    b = input ('De que pais quieres conocer su poblacion?: ')

    print ('La poblacion de '+ b + " es de " + str (dicpaises [b])+ " millones de habitantes.")


if __name__ == "__main__":
    run ()
