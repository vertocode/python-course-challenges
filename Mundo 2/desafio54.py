import datetime
year = datetime.datetime.now().date().strftime('%Y')
print(year)
maior = 0;
menor = 0;
for c in range(1, 8):
    ano = int(input('{}° Ano de nascimento: '.format(c)))
    if (int(year) - ano) >= 21: 
        maior += 1;
    else:
        menor += 1;
print('Das 7 datas de nascimento informadas, {} atingiram a maioridade e {} ainda não atingiram!'.format(maior, menor))