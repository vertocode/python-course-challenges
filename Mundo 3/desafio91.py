from random import randint
from operator import itemgetter
from time import sleep
lista = {'jogador1': randint(1,6),
         'jogador2': randint(1,6),
         'jogador3':randint(1,6),
         'jogador4':randint(1,6)}
print('=-~'*20)
print('== Sorteio dos Dados ==')
for n, v in lista.items():
    sleep(0.7)
    print(f'O {n} tirou {v}.')
ranking = [];
ranking = sorted(lista.items(), key=itemgetter(1), reverse=True)
print('=-~'*20)
print('== Ranking dos Jogadores ==')
for n,v in enumerate(ranking):
    sleep(0.7)
    print(f'{n+1}° lugar: {v[0]} com {v[1]}')
print('=-~'*20)
print('Volte Sempre!')