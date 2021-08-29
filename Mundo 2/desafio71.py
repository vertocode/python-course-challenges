print('='*20)
print('BANCO VERTO')
print('='*20)
value = int(input('Que valor você quer sacar? R$'))
m50 = 0;
m20 = 0;
m10 = 0;
m1 = 0;
while True:
    if value > 0:
        if value >= 50:
            value -= 50;
            m50 +=1
        elif value >= 20:
            value -= 20;
            m20 +=1
        elif value >= 10:
            value -= 10;
            m10 +=1
        else:
            value -= 1;
            m1 += 1
    else:
        break
print(f'Total de {m50} cédulas de R$50\nTotal de {m20} cédulas de R$20\nTotal de {m10} cédulas de R$10\nTotal de {m1} cédulas de R$1\n', '='*20)