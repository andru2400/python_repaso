def sum_rec(n):
    if n == 0:
        return n
    return n + sum_rec(n-1)

def run():    
    n = int(input('Digite un numero para hacerle la suma Recursiva:'))

    result = sum_rec(n)
    print('El resultado de la suma es {}'.format(result))


if __name__ == '__main__':
    run()
