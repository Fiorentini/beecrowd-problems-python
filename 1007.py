def main():
    a = input()
    b = input()
    c = input()
    d = input()

    dif = multiplicacao(int(a), int(b)) - multiplicacao(int(c), int(d))

    print('DIFERENCA = {}'.format(dif))


def multiplicacao(a, b):
    return a * b

if __name__  == '__main__': 
    main()