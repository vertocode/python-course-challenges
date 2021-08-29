length = 0;
maior = 0;
menor = 999999;
media = 0;
soma = 0;
nextt = 'S';
while nextt == 'S':
    nd = int(input('Digite um número: '))
    soma += nd;
    if nd > maior:
        maior = nd
    elif nd < menor:
        menor = nd
    nextt = input('Quer continuar?[ S / N ]').upper()
    length += 1;
media = soma / length
print('Analisando os {} números digitados, percebemos que o maior é o {}, o menor é o {}, a soma entre eles é igual a {}, e a média é {:.2}'.format(length, maior, menor, soma, media))