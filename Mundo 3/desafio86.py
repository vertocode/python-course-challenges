lista = []
for c in range(0, 3):
    for n in range(0, 3):
        lista.append(int(input(f'Digite um valor para [{c}, {n}]: ')))
print('-='*30)
count = 0;
for c in range(0, 9):
    print(f'[ {lista[c]} ]', end='')
    count += 1
    if count%3 == 0:
        print('')