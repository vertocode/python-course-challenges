a = float(input('1° Medida: '))
b = float(input('2° Medida: '))
c = float(input('3° Medida: '))
if a+b < c or a+c < b or c+b < a:
    print('Não é um triangulo')
else:
    print('É um triangulo')
