def ficha(nome='desconhecido',gols='0'):
    print('=-='*20)
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato. ')
    print('=-='*20)

name = input('Nome: ')
goals = input('Números de gols: ')
if len(name) > 0:
    if len(goals) > 0:
        ficha(name, goals)
    else:
        ficha(name)
elif len(goals) > 0:
    ficha(gols=goals)
else:
    ficha()