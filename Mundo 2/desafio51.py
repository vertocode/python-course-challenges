ntermo = int(input('Qual é o primeiro termo da PA?'))
razao = int(input('Qual é a razão da PA? '))
for c in range(ntermo, razao * 10 + ntermo, razao):
    print(c, end=' => ')
print('Acabou')