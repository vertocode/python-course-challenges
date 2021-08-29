l1 = int(input('Primeira medida: '))
l2 = int(input('Segunda medida: '))
l3 = int(input('Terceira medida: '))
if (l1 < (l2 + l3)) or (l2 < (l1 + l3)) or (l3 < (l1 + l2)):
    if (l1 == l2) and (l1 == l3):
        print('É um triângulo Equilátero!')
    elif ((l1 == l2) and (l1 != l3)) or ((l1 == l3) and (l1 != l2)) or ((l3 == l2) and (l3 != l1)):
        print('É um triângulo Isósceles!')
    else:
        print('É um triângulo Escaleno')
else:
    print('As medidas não formam um triângulo')