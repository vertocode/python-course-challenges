from time import sleep
def contador(i, f, p):
    if p < 0:
        while i > f-1:
            print(i, end=' ==> ')
            i += p
        print('FIM!')
    elif i < f:
        while i < f+1:
            print(i, end=' ==> ')
            i += p
        print('FIM!')
    else:
        while i > f-1:
            print(i, end=' ==> ')
            i -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)