print('Calculador de Área')
largura = float(input('Largura da parede em metros: '))
altura = float(input('Altura da parede em metros: '))
tintapinta = 2
print('Sendo a largura igual a {}m e a altura igual a {}m, então a área é igual a {}m², sendo que cada litro de tinta pinta {}m², serão gastos {} litros de tinta para pintar a parede toda.'.format(largura, altura, altura * largura, tintapinta, (altura * largura) / tintapinta))