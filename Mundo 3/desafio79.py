lista = []
res = 'S'
while res == 'S':
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Valor duplicado! Não vou adicionar...') 
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso...') 
    res = input('Que continuar?[S/N]').upper()[0]
lista.sort()
print(f'Você digitou os valores {lista}')