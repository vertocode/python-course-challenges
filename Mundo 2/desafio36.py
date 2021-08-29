valorcasa = int(input('Qual o valor da casa? R$'))
salario = int(input('Qual o seu salário? R$'))
anos = int(input('Quantos anos você vai pagar? '))
mensal = valorcasa/(anos*12)
if mensal > (salario * 0.30):
    print('Infelizmente você não pode realizar essa compra!')
else:
    print('Você pode realizar essa compra!\nvalor da parcela:R${:.2f}'.format(mensal))