from time import sleep
print('-~'*30)
print(' == Cadastro de jogadores == ')
print('-~'*30)
lista = {
    'nome' : [],
    'gols' : [],
    'total' : []
}
while True:

    #Pegando informações do cliente
    nome = input('Nome: ')
    partidas = int(input(f'Quantas partidas {nome} jogou? '))
    listagol = []
    total = 0;
    for c in range(0, partidas):
        golst = int(input(f'Quantos gols na partida {c}'))
        listagol.append(golst)
        total += golst

    #Colocando em listas
    lista['nome'].append(nome)
    lista['gols'].append(listagol)
    lista['total'].append(total)

    res = input('Quer continuar? [S/N]: ').upper()[0]
    if res == 'N':
        break

#Dando opções para o cliente
while True:
    print('=-'*30)
    print('cod   nome         gols         total')
    print('-~'*30)
    for c in range(0, len(lista['nome'])):
        print(f'{c}   {lista["nome"][c]}         {lista["gols"][c]}         {lista["total"][c]}')

    opcao = int(input('Mostras dados de qual jogador?[999 para sair] '))
    print('=-'*30)
    if opcao == 999:
        break
    elif opcao > len(lista['nome'])-1:
        print('Opção invalida. Tente novamente!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {lista["nome"][opcao]}')
        for c in range(0, len(lista['gols'])):
            sleep(1)
            print(f'No jogo {c} fez {lista["total"][c]} gols.')