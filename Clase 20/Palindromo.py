def palindromo(palabra):
    palabra = palabra.replace(" ","")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run ():
    palabra = input ("Escribe  una palabra y descubre si es un palindromo.  Ingresa tu palabra o rase: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:       
        print ("Es palíndromo")
    else:   
        print ("No es palíndromo")


if __name__ == "__main__":
    run ()
