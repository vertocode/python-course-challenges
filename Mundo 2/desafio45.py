import random
from time import sleep
#variables
player = input('PEDRA, PAPEL OU TESOURA:\n').upper()
pc = random.randint(1,3)
#transform result pc
if pc == 1:
    pc = 'PEDRA'
elif pc == 2:
    pc = 'PAPEL'
else:
    pc = 'TESOURA'
#animation
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 20)
#see who win and tell the player
if (player == 'PEDRA') and (pc == 'TESOURA') or (player == 'PAPEL') and (pc == 'PEDRA') or (player == 'TESOURA') and (pc == 'PAPEL'):
    print('Você mostrou {} e o pc {}, Você ganhou, Parabéns!'.format(player,pc))
elif player == pc:
    print('Você mostrou {} e o pc {}, Empatou!'.format(player, pc))
else:
    print('Você mostrou {} e o pc {}, Você perdeu, Tente novamente!'.format(player, pc))
print('-=' * 20)