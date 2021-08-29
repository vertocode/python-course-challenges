ntermo = int(input('Qual é o primeiro termo da PA?'))
razao = int(input('Qual é a razão da PA? '))
c = ntermo;
while razao * 9 + ntermo > c:
    c += razao;
    print(c, end=' => ')