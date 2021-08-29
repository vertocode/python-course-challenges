import random
print('Sorteador')
#Pede a quantidade de participantes
#Adicionei essa opção hehe, achei interessante
n = int(input('Quantos participantes existem no sorteio? '))
#Pede o nome de todos os participantes e armazena todos eles
participantes = []
for x in range(1, n + 1):
    participante = input('{}° participante:'.format(x))
    participantes.append(str(participante))

random.shuffle(participantes)
print('A ordem de apresentação será ')
print(participantes)