nums = (int(input('1° valor: ')), int(input('2° valor: ')), int(input('3° valor: ')), int(input('4° valor: ')))
print(f'Você digitou os valores: {nums}\nO valor 9 apareceu {nums.count(9)} vezes\nO valor 3 apareceu na posição {nums.index(3)+1}°\nOs números pares foram ', end='')
for c in nums:
    if c % 2 == 0:
        print(c, end=', ')
print('\n')