print('Calculador de tipos')
algo = input('Digite qualquer coisa: ')
print('O tipo primitivo do que você escreveu é {}'.format(type(algo)))
print('é alfanumérico? ' , algo.isalnum())
print('é alpha? ' , algo.isalpha())
print('é ASCII? ' , algo.isascii())
print('é Decimal? ' , algo.isdecimal())
print('é Digito? ' , algo.isdigit())
print('é apenas letras minúsculas? ' , algo.islower())
print('é apenas letras maiúsculas? ' , algo.isupper())
print('é espaço? ' , algo.isspace())