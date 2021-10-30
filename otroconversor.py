dolares = input("¿Cuántos dólares tienes?: ")
dolares = float(dolares)
valor_dolar = float(19.05)
pesos = dolares * valor_dolar
pesos=round(pesos,2)
pesos = str(pesos)
print("Tienes $" + pesos + " pesos")