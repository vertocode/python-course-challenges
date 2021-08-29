nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('REPROVADO!')
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÃO')
elif media > 6.9:
    print('APROVADO')
else:
    print('Nota inválida!')