print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)
maisdemil = 0;
menor = 99999999999999;
soma = 0;
while True:
    nome = input('Nome do Produto: ')
    preco = int(input('Preço: R$'))
    nextt = input('Quer continuar? [ S/N ]: ').upper()
    soma += preco
    if preco > 1000:
        maisdemil += 1;
    if preco < menor:
        menor = preco;
        menorn = nome; 
    if nextt == 'N':
        break
print('-'*10,'FIM DO PROGRAMA','-'*10)
print(f'O total da compra foi R${soma}\nTemos {maisdemil} custando mais de R$1000.00\nO produto mais barato foi {menorn} que custa R${menor}')