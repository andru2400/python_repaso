import random


def run():
    number_found = False
    number_start = int(input('Ingrese número de inicio de rango: '))
    number_end = int(input('Ingrese número de tamaño de rango: '))

    random_number = random.randint(number_start, number_end)

    while not number_found:
        number = int(input('Intenta un número: '))

        if number == random_number:
            print('Felicidades, encontraste el número')
            number_found = True
        elif number > random_number:
            print('El número es más pequeño')
        else:
            print('El numero es más grande')


if __name__ == '__main__':
    run()
