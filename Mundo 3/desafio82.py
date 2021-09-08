lista = []
res = 'S'
while res == 'S':
    lista.append(int(input('Digite um número: ')))
    res = input('Quer continuar?[S/N]').upper()[0]
par = []
impar = []
for c in lista:
    if c%2 == 0:
        par.append(c)
    else:
        impar.append(c)
print('-='*30)
print(f'lista:{lista}\npares:{par}\nímpares:{impar}')