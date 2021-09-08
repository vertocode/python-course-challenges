lista = []
for c in range(0, 5):
    lista.append(int(input('Digite um valor para a Posição {}: ')))
    lista2 = lista[:]
    lista2.sort()

pmaior = 0;
while lista2[-1] != lista[pmaior]:
    pmaior += 1;

pmenor = 0;
while lista2[0] != lista[pmenor]:
    pmenor += 1;

print('=='*20)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {lista2[-1]} na posição {pmaior+1}' )
print(f'O menor valor digitado foi {lista2[0]} na posição {pmenor+1}' )