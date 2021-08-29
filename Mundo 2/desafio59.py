n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
function = int(input('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n'))
while function == 4:
    n1 = int(input('Digite o 1° número: '))
    n2 = int(input('Digite o 2° número: '))
    function = int(input('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n')) 
if function == 1:
    somar = n1 + n2
    print('='*11,somar,'='*11)
elif function == 2:
    multiplicar = n1 * n2
    print('='*11,multiplicar,'='*11)
elif function == 3:
    if n1 > n2:
        maior = n1
    else:
        maior = n2
    print('='*11,maior,'='*11)