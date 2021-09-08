print('='*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('='*40, end='')
produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
count = 0;
for c in produtos:
    if c == str(c):
        print(f'\n{produtos[count]:.<30}.........R$ {produtos[count + 1]:>5.2f}', end='')
    count += 1
print('\n','='*40)