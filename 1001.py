def main():
    a = input()
    b = input()

    c = soma(int(a), int(b))

    print('X = {}'.format(c))


def soma(a, b):
    return a + b

if __name__  == '__main__': 
    main()