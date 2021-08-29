f = input('Digite uma frase: ')
f1 = f.replace(' ','')
if f1 == f1[::-1]:
    print('{} é um palíndromo'.format(f))
else:
    print('{} não é um palíndromo'.format(f))
