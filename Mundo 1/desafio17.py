import math
print('Calculador de triangulo retângulo')
n1 = float(input('Qual o valor do cateto oposto? '))
n2 = float(input('Qual o valor do cateto adjacente? '))
res = math.hypot(n1, n2)
print('A hipotenusa é {:.1f}'.format(res))
