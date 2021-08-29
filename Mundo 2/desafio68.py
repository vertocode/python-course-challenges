from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
win = 0;
while True:
    value = int(input('Diga um valor: '))
    pc = randint(1, 15)
    if (value+pc)%2 == 0:
        print('-' * 20)
        print(f'Você jogou {value} e o computador {pc}. Total de {value+pc}, [DEU PAR]')
        print('-' * 20)
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        win += 1
    else:
        print('-' * 20)
        print(f'Você jogou {value} e o computador {pc}. Total de {value+pc}, [DEU ÍMPAR]')
        print('-' * 20)
        print('Você PERDEU!')
        print('-' * 20)
        break
print(f'GAME OVER! Você venceu {win} vezes.')
print('-' * 20)