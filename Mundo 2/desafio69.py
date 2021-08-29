maioridade = 0;
homens = 0;
mulhermenor = 0;
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    sexo = 's'
    while sexo not in 'MF':
        sexo = input('Sexo: [ M/F ]: ').upper()[0]
    print('-'*20)
    if idade > 18:
        maioridade += 1;
    if sexo == 'M':
        homens += 1;
    if sexo == 'F':
        if idade < 20:
            mulhermenor += 1;
    nextt = input('Quer continuar? [S/N]: ').upper()
    if nextt == 'N':
        break;
print('=-'*20)
print(f'Total de pessoas com mais de 18 anos é igual a {maioridade}\nAo todo temos {homens} homens cadastrados\nE temos {mulhermenor} mulheres com menos de 20 anos')
print('=-'*20)