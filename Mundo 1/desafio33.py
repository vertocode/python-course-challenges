n1 = int(input('1° Número: '))
n2 = int(input('2° Número: '))
n3 = int(input('3° Número: '))

if n1 > n2 and n1 > n3:
    print(n1, ' é o maior número!')
elif n2 > n1 and n2 > n3:
    print(n2, ' é o maior número!')
else:
    print(n3, ' é o maior número!')

if n1 < n2 and n1 < n3:
    print(n1, ' é o maior número!')
elif n2 < n1 and n2 < n3:
    print(n2, ' é o maior número!')
else:
    print(n3, ' é o maior número!')