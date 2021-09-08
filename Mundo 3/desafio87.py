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
print('-='*30)
soma = 0;
terc = 0;
seg = 0;
count = 0;
for c in lista:
    count += 1;
    if c%2 == 0:
        soma += c
    if count == 3 or count == 6 or count == 9:
        terc += c
    if count > 3 and count < 7:
        if count == 4:
            seg = c
        else:
            if c > seg:
                seg = c;
            else:
                break
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {terc}')
print(f'O maior valor da segunda linha é {seg}')