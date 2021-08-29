n = input('Digite um número: ')
n = list(n)
unidade = n[len(n) - 1]
dezena = n[len(n) - 2]
centena = n[len(n) - 3]
milhar = n[len(n) - 4]
if (len(n) == 1):
    print('Unidade:{}'.format(unidade))
elif (len(n) == 2):
    print('Unidade:{}\nDezena:{}'.format(unidade, dezena))
elif (len(n) == 3):
    unidade = n[len(n) - 1]
    dezena = n[len(n) - 2]
    print('Unidade:{}\nDezena:{}\nCentena:{}'.format(unidade, dezena, centena))
else:
    print('unidade:{}\ndezena:{}\ncentena:{}\nmilhar:{}'.format(unidade, dezena, centena, milhar))