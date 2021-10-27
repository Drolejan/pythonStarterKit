def imprimir_mensaje():
    print('Mensaje especial: ')
    print('¡Estoy aprendiendo a usar funciones!')


imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

def print_mensaje(mensaje):
    print(mensaje)

def conversacion(mensaje):
    print('¿Cómo estás?')
    print(mensaje)
    print('¿Qué tal?')

# def conversacion(mensaje):
#     print('Hola')
#     print('Cómo estás')
#     print(mensaje)
#     print('Adios')

opcion = int(input('Elige una opción: '))
if opcion == 1:
    conversacion('Elegiste la opción 1')
elif opcion == 2:
    conversacion('Elegiste la opción 2')
else:
    print('Elige una opción válida')

# opcion = int(input('Elige una opción (1, 2, 3): '))
# if opcion == 1:
#     conversacion('Elegiste la opción 1')
# elif opcion == 2:
#     conversacion('Elegiste la opción 2')
# elif opcion == 3:
#     conversacion('Elegiste la opción 3')
# else:
#     print('Escribe la opción correcta')

def suma(a,b):
    print('Sumar dos números')
    resultado = a + b
    return resultado

sumatoria = suma(5,10)
print(sumatoria)

# def suma(a, b):
#     print('Se suman dos números')
#     resultado = a + b
#     return resultado

# sumatoria = suma(1, 4)
# print(sumatoria)