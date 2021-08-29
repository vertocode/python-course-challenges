peso = []
maior = 0;
menor = 999999;
for c in range(1, 6):
    peso.append(float(input('{} peso:'.format(c))))
    if peso[len(peso)-1] > maior:
        maior = peso[len(peso)-1]
    if peso[len(peso)-1] < menor:
        menor = peso[len(peso)-1]
print('Dos 5 pesos pedidos,\n{}\nO maior foi {}kg\n{}\nO menor foi {}kg\n{}'.format('-=' * 11, maior, '-=' * 11, menor, '-=' * 11))