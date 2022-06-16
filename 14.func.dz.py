while True:

    a = float(input('Vvedite pervoe chislo: '))
    if a == 0:
        print('spasibo')
        break
    b = input('Vvedite znak +,-,/,* : ')
    c = float(input('Vvedite vtoroe chislo: '))
    def calkul(a,c,b):
        if b == '*':
            return a * c
        elif b == '-':
            return a - c
        elif b == '/':
            try:
                return a / c
            except ZeroDivisionError:
                print('oshibka delenija na 0')
        elif b == '+':
            return a + c
        else:
            print('net takoy apperacii')
            return 'ne vern znak'
    print('Otvet: ', calkul(a,c,b))
#

