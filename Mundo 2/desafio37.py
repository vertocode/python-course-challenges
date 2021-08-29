n = int(input('Digite um número: '))
type = int(input('Digite:\n1 para binário\n2 para octal\n3 para hexadecimal\n:'))
if type == 1:
    print(bin(n)[2:])
elif type == 2:
    print(oct(n)[2:])
elif type == 3:
    print(hex(n)[2:])
else:
    print('Tipo de número invalido!')