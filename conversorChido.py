# menu = """
# Bienvenido al conversor de monedas 🤡
# 1. Pesos colombianos a dolares
# 2. Pesos mexicanos a dolares
# 3. Pesos argentinos a dolares

# Elige una opción:
# """

# opcion = int(input(menu))
# if opcion == 1:
#     pesos = float(input('¿Cuántos pesos colombianos tienes?: '))
#     dolares = pesos / 3200
#     print(f'${dolares:.2f}')
# elif opcion == 2:
#     pesos = float(input('¿Cuántos pesos mexicanos tienes?: '))
#     dolares = pesos / 20
#     print(f'${dolares:.2f}')
# elif opcion == 3:
#     pesos = float(input('¿Cuántos pesos argentinos tienes?: '))
#     dolares = pesos / 2550
#     print(f'${dolares:.2f}')
# else:
#     print('Opción inválida')

# def conversor(tipo_pesos, valor_dolar):
#     pesos = float(input(f'¿Cuántos {tipo_pesos} tienes?: '))
#     dolares = pesos / valor_dolar
#     print(f'${dolares:.2f}')

def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")


menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print('Ingresa una opción correcta por favor')