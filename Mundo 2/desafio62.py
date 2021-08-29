ntermo = int(input('Qual é o primeiro termo da PA?'))
razao = int(input('Qual é a razão da PA? '))
print(ntermo, end=' => ')
c = 0;
print('\n','==' * 11)
while razao * 9 + ntermo > c:
    c += razao;
    print(c, end=' => ')
print('\n','==' * 11)
mais = 'a'
while mais != 0:
    mais = int(input('\nQuer mais termos? quantos?(Digite 0 se não querer)'))
    c1 = c;
    print('==' * 11)
    while razao * mais + c1 > c:
        c += razao;
        print(c, end=' => ')
    print('\n','==' * 11)
