def header_pyhelp():
    print('\33[30;42m-' * 35 + f'\n{"SISTEMA DE AJUDA PyHelp":^35}\n' + '-' * 35)


def header_search_pyhelp(search):
    header = f'Acessando o manual do comando "{search}"'
    print('\33[30;44m~' * (len(header) + 4))
    print(f'  {header}  ')
    print('~' * (len(header) + 4))


def pyhelp(search):
    header_search_pyhelp(search)
    print('\33[37;40m', end='')
    return help(search)


while True:
    header_pyhelp()
    pesquisa = input('\33[mFunção ou Biblioteca >>> ').strip().lower()

    if pesquisa.upper() == 'FIM':
        print('\33[30;41m=' * 20 + f'\n{"FINALIZADO":^20}\n' + '=' * 20)
        break

    pyhelp(pesquisa)