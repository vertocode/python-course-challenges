peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura ** 2)
print('Seu IMC é {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso!')
    print('Se cuide!')
elif imc >= 18.5 and imc < 25:
    print('Você está com o peso ideal!')
elif imc >= 25 and imc > 30:
    print('Você está em sobrepeso!')
    print('Se cuide!')
elif imc >= 30 and imc > 40:
    print('Voce está com obesidade!')
    print('Se cuide!')
else:
    print('Você está com Obesidade mórbida!')
    print('Se cuide!')