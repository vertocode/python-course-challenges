col = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo', 'Corinthians', 'Atlético-GO', 'Ceará', 'Athletico-PR', 'Internacional', 'Fluminense', 'Santos', 'Juventude', 'São Paulo', 'Cuiabá', 'Bahia', 'América-MG', 'Grêmio', 'Sport', 'Chapecoense')
sea = col.index('Chapecoense') + 1
print(f'Os 5° primeiros colocados são {col[:5]}')
print(f'Os ultimos 4 colocados são {col[-4:]}')
print(f'Os colocados em ordem alfabética: {sorted(col)}')
print(f'O Chapecoense se encontra na {sea}° posição')