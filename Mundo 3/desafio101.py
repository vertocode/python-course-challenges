from datetime import date
datetoday = int(date.today().strftime('%Y'))
def voto(age):
    if age > 15 and age < 18:
        return 'VOTO OPCIONAL'
    elif age > 17:
        return 'VOTO OBRIGATÓRIO!'
    else:
        return 'NÃO VOTA'
    
age = int(date.today().strftime('%Y')) - int(input('Ano de nascimento: '))
state = voto(age)
print(f'Com {age} anos: {state}')