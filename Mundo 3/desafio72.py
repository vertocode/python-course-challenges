num = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
res = int(input('Digite um número entre 0 e 20:\n'))

while res > 20 or res < 0:
    res = int(input('Tente novamente. Digite um número entre 0 e 20:\n'))
print(f'Você digitou o número {num[res-1]}')