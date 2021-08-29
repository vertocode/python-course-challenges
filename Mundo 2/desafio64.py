nd = 0;
n = 0;
while nd != 999:
    nd = int(input('[DIGITE 999 PARA PARAR O PROGRAMA]\nDigite um número para acumular uma soma:'))
    n = n + nd
print('A soma de todos os números digitados é igual a {}'.format(n - 999))