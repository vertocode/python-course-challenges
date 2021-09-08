from random import randint
from time import sleep
n = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'Sorteando {n} jogos')
lista = []
jogos = []
tot = 1
while tot <= n:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1;
        if cont>= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1;
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('Boa sorte!')