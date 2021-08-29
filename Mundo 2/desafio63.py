n = int(input('Quantos termos: '))
ultimo = 1;
penultimo = 1;

if(n==1):
    print('1 -> ', end='')
elif(n==2):
    print('1 -> ', end='')
    print('1 -> ', end='')
else:
    count = 3
    print('1 -> ', end='')
    print('1 -> ', end='')
    while count < n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
        print(termo, '-> ', end='')
print('FIM!')