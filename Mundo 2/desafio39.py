import datetime
ano = int(input('Ano de nascimento: '))
dataatual = datetime.date.today()
year = int(dataatual.strftime('%Y'))
idade = year - ano
if idade > 18:
    print('Ja passou o tempo de você se alistar faz {}anos'.format(idade - 18))
elif idade >= 17:
    print('Você já está no tempo do seu alistamento!')
else:
    print('Ainda falta {}anos para o seu alistamento!'.format(18 - idade))