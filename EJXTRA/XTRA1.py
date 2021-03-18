# def run ():
    # Edad = int (input ("Capture su Edad en años humano: "))
    # nombre = input ("Capture su nombre de perro: ")
    # Edad_Perro = Edad * 7
    # print ("Hola, soy " + nombre + " tengo " + str (Edad_Perro) + " años perro.")


    # print('Suma de dos enteros')
    # a = int( input('Entre el dato 1: ') )
    # b = int( input('Entre el dato 2: ') )
    # suma = a + b
    # print('La suma vale:' , suma)

    # print('Suma de dos reales')
    # c = float( input('Entre el dato 1: ') )
    # d = float( input('Entre el dato 2: ') )
    # sumar = c + d
    # print('La suma vale:' , sumar)

    # print('Pruebas de formatos de impresión')
    # print('--------------------------------\n')
    # # Inicializamos las variables
    # dato1 = int (input ("Captura un numero entero para dato uno: "))
    # dato2 = float (input ("Captura un numero con decimales para dato dos: "))
    # dato3 = input ('Captura un texto: ')
    # # Pruebas
    # print(f'Entero en bases 10, 2 y 16 : {dato1} {dato1:b} {dato1:x}')
    # print(f'Entero alineado derecha (6 pos rell 0) : {dato1:06}')
    # print(f'Real sin formato : {dato2}')
    # print(f'Real con dos decimales : {dato2:.2f}')
    # print(f'Real alineado derecha (12 pos 0 decim) : {dato2:12.0f}')
    # print(f'Real alineado derecha (12 pos 2 decim) : {dato2:12.2f}')
    # print(f'Real con formato exponencial : {dato2:e}')
    # print(f'Cadena alin. izquierda (20 pos rell =) : {dato3:=<20}')
    # print(f'Cadena centrada (20 pos rell _) : {dato3:_^20}')
    # print(f'Cadena alin. derecha (20 pos rell .) : {dato3:.>20}')

    # print('Pruebas de formatos de impresión')
    # print('--------------------------------\n')
    # # Inicializamos las variables
    # dato4 = int (input ("Captura un numero entero para dato cuatro: "))
    # dato5 = float (input ("Captura un numero con decimales para dato cinco: "))
    # dato6 = input ('Captura un texto: ')
    # # Pruebas
    # print('Entero en bases 10 y 16 : %d %x' % (dato4 , dato4))
    # print('Entero alineado derecha (6 pos rell 0) : %06i' % (dato4))
    # print('Real sin formato : %f' % (dato5))
    # print('Real con dos decimales : %.2f' % (dato5))
    # print('Real alineado derecha (12 pos 0 decim) : %12.0f' % (dato5))
    # print('Real alineado derecha (12 pos 2 decim) : %12.2f' % (dato5))
    # print('Real con formato exponencial : %e' % (dato5))
    # print('Cadena alin. izquierda (20 pos) : %20s' % (dato6))
    # print('Cadena alin. derecha (20 pos) : %-20s' % (dato6))

m01 = 'Matematicas'
m02 = 'Lengua Extranjera'
m03 = 'Literatura'
m04 = 'Fisica'
m05 = 'Filosofia'

def recaptura ():
    print ("Por favor vuelva a capturar, le dije del 0 al 10, No sea Chango")

def run ():
    print ('Bienvenido al programa de calificaciones de Changuito INC.')
    print ('Por favor capture las calificaciones en numeros con dos decimales del 0 al 10')
    
    m1 = float(input ( str (m01) + ': '))
    m2 = float(input ( str (m02) + ': '))
    m3 = float(input ( str (m03) + ': '))
    m4 = float(input ( str (m04) + ': '))
    m5 = float(input ( str (m05) + ': '))

    while m1 > 10:
        recaptura ()
        m1 = float(input ( m01 + ': '))
    
    while m2 > 10:
        recaptura ()
        m2 = float(input ( m02 + ': '))

    while m3 > 10:
        recaptura ()
        m3 = float(input ( m03 + ': '))
   
    while m4 > 10:
        recaptura ()
        m4 = float(input ( m04 + ': '))

    while m5 > 10:
        recaptura ()
        m5 = float(input ( m05 + ': '))

    sumamaterias = m1 + m2 + m3 + m4 + m5

    promedio = sumamaterias / 5

    print ('El promedio obtenido es de ' + str (promedio) + " puntos.")

    if promedio >= 6:
        print ('Con ese promedio usted paso de ciclo escolar')
    else:
        print (' Con tan solo ' + str (promedio) + ' usted es el eslabon perdido, vuelva a cursar de ciclo para que se le quite lo burrales')

if __name__ == "__main__":
    run ()
