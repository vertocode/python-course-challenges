sexo = input('sexo[ M / F ]:').strip().upper()[0]
while sexo not in 'MF':
    sexo = input('sexo[ M / F ]:').strip().upper()[0]
print('Fim!')