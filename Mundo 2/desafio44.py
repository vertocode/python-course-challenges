price = float(input('Digite o valor normal do produto: '))
type = int(input('Qual a forma de pagamento?\n[1]À vista no dinheiro/cheque:10% de desconto\n[2]À vista no cartão:5% de desconto\n[3]em até 2x no cartão: preço normal\n[4]3x ou mais no cartão: 20% de juros\nDigite um número de acordo com a opção desejada!'))
if type == 1:
    print('Valor a pagar: R${:.2f}'.format(price - (price * 0.10)))
elif type == 2:
    print('Valor a pagar: R${:.2f}'.format(price - (price * 0.05)))
elif type == 3:
    print('Valor a pagar: R${:.2f}'.format(price))
elif type == 4:
    print('Valor a pagar: R${:.2f}'.format(price + (price * 0.20)))