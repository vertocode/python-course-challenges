lista = [[],[[],[]],[]]
print('='*30)
while True:
    nome = input('Nome: ')
    lista[0].append(nome)
    nota1 = float(input('Nota 1: '))
    lista[1][0].append(nota1)
    nota2 = float(input('Nota 2: '))
    lista[1][1].append(nota2)
    media = (nota1 + nota2) / 2
    lista[2].append(media)
    print('='*30)
    resp = input('Quer continuar? [S/N]: ')
    print('='*30)
    if resp in 'Nn':
        break
while True:
    print('='*30)
    print('No.  NOME      MÉDIA')
    print('-'*30)
    for c in range(0, len(lista[0])):
        print(f'{c} {lista[0][c]}    {lista[2][c]}')
    res = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if res < len(lista[0]):
        for c in range(0, len(lista[0])):
            if res == c:
                print('='*30)
                print(f'Notas de {lista[0][c]} são {lista[1][0][c]} e {lista[1][1][c]}')

    elif res == 999:
        break
    else:
        print('='*30)
        print('Aluno inválido! Tente novamente.')
print('='*30)
print('Volte sempre!')
print('='*30)