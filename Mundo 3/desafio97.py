def escreva(str):
    print('=' * len(str))
    print(str)
    print('=' * len(str))
while True:
    t = input('Digite um texto: ')
    escreva(t)
    r = input('Quer continuar? [S/N]: ').upper()[0]
    if r == 'N':
        break
escreva('VOLTE SEMPRE!')