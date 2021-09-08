lista = []
par = []
impar = []
lista.append(par)
lista.append(impar)
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor%2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
par.sort()
impar.sort()
print(f'pares: {par}\nímpares: {impar}')