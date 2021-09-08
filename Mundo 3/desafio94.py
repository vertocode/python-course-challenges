lista = {}
nome = []
sexo = []
idade = []
while True:
    nome.append(input('Nome: '))
    lista['nome'] = nome
    sexo.append(input('Sexo: [M/F] ').upper()[0])
    lista['sexo'] = sexo
    idade.append(int(input('Idade: ')))
    lista['idade'] = idade
    res = input('Quer continuar? [ S / N ]: ').upper()[0]
    if res == 'N':
        break
somaidade = 0;
for c in idade:
    somaidade += c;
    lista['somaidade'] = somaidade
mulheres = []
for n,c in enumerate(sexo):
    if c == 'F':
        mulheres.append(nome[n])
lista['mulheres'] = mulheres
media = somaidade / len(lista['nome'])
print(f' - O grupo tem {len(lista["nome"])}')
print(f' - A média de idade é de {media}')
print(f' - As mulheres cadastradas foram: {mulheres}')
print(f'Lista de pessoas que estão acima da média: ')
for c in range(0, len(nome)):
    if media < idade[c]:
        print(f' -Nome = {nome[c]}; sexo = {sexo[c]}; idade = {idade[c]}')