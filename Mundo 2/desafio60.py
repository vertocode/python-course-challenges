n = int(input('Digite um número: '));
nf = n
c=n;
while c != 1:
    c -= 1
    n = n * c
print('{}!'.format(nf),'=',n)