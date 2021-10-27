pesos = input("Cuantos pesos quieres convertir a dolares: ")
pesos = float(pesos)
valor_dolar = float(19.05)
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dolares")