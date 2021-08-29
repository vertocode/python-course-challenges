nome = []
idade = []
sexo = []
for c in range(1, 5):
    print('========= {}° PESSOA ========='.format(c))
    nome.append(input('{}° Nome: '.format(c)))
    idade.append(int(input('{}° idade: '.format(c))))
    sexo.append(input('{}° sexo[F] ou [M]: '.format(c)))
def CalcularMedia(idade):
    valor = 0;
    for m in range(0, 4):
        valor += idade[m]
    valor = valor / len(idade)
    return valor;
def HomemMaisVelho(idade, sexo):
    valor = 0
    for m in range(0, 4):
        if sexo[m] == 'M' or sexo[m] == 'm':
            if idade[m] > idade[m - 1]:
                valor = m
    return valor;
def MulheresMenosDe20Anos(idade, sexo):
    n = 0;
    for m in range(0, 4):
        if sexo[m] == 'F' or sexo[m] == 'f':
            if idade[m] < 20:
                n = n + 1
    return n;
MediaIdade = CalcularMedia(idade)
MMaisVelho = nome[HomemMaisVelho(idade, sexo)]
FMenosDe20anos = MulheresMenosDe20Anos(idade, sexo)
print('{}\nDesafio 56\n{}\nA média de idade do grupo é {}\n{}\nO nome do homem mais velho do grupo é o {}\n{}\nO grupo possui {} mulheres com menos de 20 anos!\n{}\nOBRIGADO POR PARTICIPAR!'.format('-=' * 11, '-=' * 11, MediaIdade, '-=' * 11, MMaisVelho, '-=' * 11, FMenosDe20anos, '-=' * 11))