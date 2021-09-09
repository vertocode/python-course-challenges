def area(a, b):
    c = a * b
    print('-='*30)
    print(f'A área de um terreno {a}x{b} é de {c}m².')
    print('-='*30)

    
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m):'))
area(a, b)