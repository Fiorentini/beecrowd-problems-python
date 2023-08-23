def main():
    a = input()
    b = input()

    c = multiplicacao(int(a), int(b))

    print('PROD = {}'.format(c))


def multiplicacao(a, b):
    return a * b

if __name__  == '__main__': 
    main()