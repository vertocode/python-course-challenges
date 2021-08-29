s = int(input('Salário em R$'))
if s > 1250:
    print('Salário novo: R${}'.format(s + (s * 0.10)))
else:
    print('Salário novo: R${}'.format(s + (s * 0.15)))