import datetime
date = datetime.date.today()
datenow = int(date.strftime('%Y'))
ano = int(input('Ano de nascimento: '))
idade = datenow - ano
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')