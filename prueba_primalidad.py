def es_primo(numero): # Función que devuelve True si el número es primo, crear otra diferente
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False

def esPrimo(numero):
    raiz_cuadrada = numero ** 0.5
    for i in range(2, int(raiz_cuadrada) + 1):
        if numero % i == 0:
            return False
    return True


def run():
    numero = int(input('Escribe un número: '))
    if esPrimo(numero):
        print('Es primo')
    else:
        print('No es primo')


if __name__ == '__main__':
    run()
