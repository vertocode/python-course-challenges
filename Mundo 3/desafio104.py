def leiaint(m):
    s = False
    v = 0
    while True:
        n = input('\033[0;34m'+m+'\033[m')
        if n.isnumeric():
            v = int(n)
            s = True;
        else:
            print('\033[0;31m[ERRO]! Digite um número inteiro válido.\033[m')
        if s:
            break
    return v


num = leiaint('Digite um número: ')
print(f'Você digitou o número {num}')