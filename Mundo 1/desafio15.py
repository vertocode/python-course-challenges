print('Aluguel de Carros')
d = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
print('Valor a pagar: R${:.2f}'.format((d*60)+(km*0.15)))