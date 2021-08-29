print('Aumento de salário')
salario = float(input('Salário: '))
aumento = float(15)
print('Salario de R${} teve um aumento de {}%\nNovo salário é igual a R${}'.format(float(salario), float(aumento), float(salario + (salario*aumento)/100)))