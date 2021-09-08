lista = []
res = 'S'
count = 0;
while res == 'S':
    lista.append(int(input('Digite um valor: ')))
    res = input('Quer continuar?[S/N]').upper()[0]
    count += 1;
lista.sort(reverse=True)
print(f'Tem {count} elementos')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('Tem 5!')