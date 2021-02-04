# def imprimir_mensaje ():
#     print ("Mensaje Especial")
#     print ("ESTOY APRENDIENDO A USAR FUNCIONES!")

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

opcion = input ("Elige una opción 1, 2, 3:  ")
opcion = int (opcion)

# if opcion == 1:
#     print("¡HOla!")
#     print("¿Cómo estás?")
#     print("Elegiste la opción 1")
#     print("¡Adiós!")
# elif opcion == 2:
#     print("¡HOla!")
#     print("¿Cómo estás?")
#     print("Elegiste la opción 2")
#     print("¡Adiós!")
# elif opcion == 3:
#     print("¡HOla!")
#     print("¿Cómo estás?")
#     print("Elegiste la opción 3")
#     print("¡Adiós!")
# else:
#     print ("Elegiste ser un macaco")

def conversacion(mensaje):
    print("¡HOla!")
    print("¿Cómo estás?")
    print(mensaje)
    print("¡Adiós!")

if opcion == 1:
    conversacion("Elegiste la opción 1")
    
elif opcion == 2:
    conversacion("Elegiste la opción 2")

elif opcion == 3:
    conversacion("Elegiste la opción 3")

else:
    print ("Elegiste ser un macaco")