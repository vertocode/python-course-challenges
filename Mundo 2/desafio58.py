from random import randint
player = int(input('Tente adivinhar qual número o pc pensou de 0-10: '))
pc = randint(0, 10)
count = 1;
while player != pc:
    player = int(input('Você errou, tente até acertar(0-10): '))
    count += 1
print('Você acertou! foi necessário {} vezes para acertar'.format(count))