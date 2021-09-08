from datetime import date
year = date.today().strftime('%Y')
print('=~='*30)
dic = {}
dic['nome'] = input('Nome: ')
nascimento =  int(input('Ano de Nascimento: '))
idade = int(year) - nascimento
dic['idade'] = idade
dic['cttps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dic['cttps'] != 0:
    dic['ano de contratação'] = int(input('Ano de Contratação: '))
    dic['salario'] = int(input('Salário: R$ '))
    aposentadoria = ((dic['ano de contratação'] - int(year)) + 35) + idade
print('-=~'*30)
print(dic)
print(f'nome tem o valor {dic["nome"]}')
print(f'idade tem o valor {dic["idade"]}')
if dic['cttps'] != 0:
    print(f'contratação tem o valor {dic["ano de contratação"]}')
    print(f'salário tem o valor {dic["salario"]}')
    print(f'aposentadoria tem o valor {aposentadoria}')
print('-=~'*30)