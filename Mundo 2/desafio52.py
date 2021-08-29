n = int(input('Digite um número: '))
v = 0;
for c in range(1, n+1):
    r = n % c
    if r == 0:
        v += 1
if v == 2:
    print('É um número primo!')
else:
    print('Não é um número primo!')
print(v)