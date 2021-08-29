print('Conversor de Real para Dolar')
n = float(input('Digite um valor em R$: '))
#Para atualizar o programa, basta apenas digitar o valor do dolar atual abaixo
valordolar = 3.27
print('{:.3}R$ é igual a {:.3}$'.format(float(n), float(n) * float(valordolar)))