lista = {
    'nome': '', 
    'media': '', 
    'situacao': ''
    }
lista['nome'] = input('Nome: ')
lista['media'] = float(input(f'Média de {lista["nome"]}: '))
print(f'Nome é igual a {lista["nome"]}')
print(f'Média é igual a {lista["media"]}')
if lista['media'] < 6:
    lista['situacao'] = 'Reprovado!'
else:
    lista['situacao'] = 'Aprovado!'
print(f'Situação é igual a {lista["situacao"]}')