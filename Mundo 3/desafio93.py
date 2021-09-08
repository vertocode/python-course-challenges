lista = {}
lista['nome'] = input('Nome do jogador: ')
n = int(input(f'Quantas partidas {lista["nome"]} jogou? '))
gols = []
lista['gols'] = gols
for c in range(0, n):
    gols.append(int(input(f'Quantos gols na partida {c}: ')))
    total = len(gols)
    lista['total'] = total
print('-='*30)
print(f'O jogador {lista["nome"]} jogou {len(gols)} partidas.')
for c in range(0, len(gols)):
    print(f'    => Na partida {c}, fez {gols[c]} gols.')