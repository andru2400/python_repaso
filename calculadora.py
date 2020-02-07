def foreign_exchange_calculator(ammount):
    mex_to_col_rate = 181.72
    return mex_to_col_rate * ammount


def run():
    print("/////////////////////////////////////////////")
    print("=                     ==                    =")
    print("=                  ========                 =")
    print("=                 ==       ==               =")
    print("=                 ==                        =")
    print("=                 ==========                =")
    print("=                          ==               =")
    print("=                 ==       ==               =")
    print("=                  =========                =")
    print("=                      ==                   =")
    print("/////////////////////////////////////////////")
    print(' C A L C U L A D O R A  D E  D I V I S A S')
    print(' Convierte pesos Mexicanos a Colombianos')
    print(' ')

    ammount = float(
        input('Ingresa el numero de pesos Mexicanos, que quieres convertir : '))
    result = foreign_exchange_calculator(ammount)

    print('${} Pesos mexicanos son ${} pesos Colombianos'.format(ammount, result))


if __name__ == '__main__':
    run()
