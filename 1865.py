def main():

    repetitions = input()

    for rep in range(0, int(repetitions)):

        heroi = input()
        name = heroi.split(' ')[0]

        if(name == 'Thor'):
            print('Y')
        else:
            print('N')
        
    
if __name__  == '__main__': 
    main()