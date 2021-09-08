from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),)
print(f'Os números sorteados foram {num}')
maior = num[0]
menor = num[0]
for c in num:
    if c > maior:
        maior = c
    if c < menor:
        menor = c
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')