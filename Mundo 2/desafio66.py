n = 0;
c = 0;
while True:
    c += 1;
    nd = int(input('Digite um valor (999 para parar): '))
    n += nd;
    if nd == 999:
        n -= 999;
        c -= 1;
        break     
print(f'A soma dos {c} valores foi {n}!')