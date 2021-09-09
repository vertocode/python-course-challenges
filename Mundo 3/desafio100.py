from random import randint
numeros = []
def sorteio(lista):
    for c in range(0, 5):
        n = randint(0, 100)
        lista.append(n)
    print(f'Foram sorteados {lista}.')


def somaPar(lista):
    sorteio(lista)
    par = 0;
    for c in lista:
        if c%2 == 0:
            par += c;
    print(f'Somando os valores pares temos o número {par}')

    
somaPar(numeros)