import math
print('Conversor de radianos para Seno, Cosseno e Tangente')
x = float(input('Digite um valor em radianos: '))
seno = math.sin(math.radians(x))
cosseno = math.cos(math.radians(x))
tangente = math.tan(math.radians(x))
print('Seno de {}° é igual a {:.2f}\nCosseno de {}° é igual a {:.2f}\nTangente de {}° é igual a {:.2f}'.format(x, seno, x,cosseno, x, tangente))