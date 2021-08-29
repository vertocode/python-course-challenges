km = int(input('Distancia da viagem em KM: '))
if km <= 200:
    print('Valor: R${:.2f}'.format(km * 0.5))
else:
    print('Valor: R${:.2f'.format(km * 0.45))