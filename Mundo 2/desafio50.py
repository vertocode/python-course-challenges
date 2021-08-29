r = 0
for c in range(1, 7):
    n = int(input('{}° Número: '.format(c)))
    if n%2 == 0:
        r += n
print(r)