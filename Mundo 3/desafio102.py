def fatorial(n, show=False):
    print('-=' *30)
    print(f'{n}! = ', end='')
    for c in range(n, 1, -1):
        c -= 1
        n *= c
        if show==True:
            if c == 1:
                print(f'{c} = ', end='')
                break
            print(f'{c} x ', end='')
    print(n)
    print('-=' *30)
fatorial(5)
fatorial(5, show=True)