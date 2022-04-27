largura = float(input('Digite a largura de sua parede em metros: '))
altura = float(input('Agora digite a altura da sua parede em metros: '))
total = largura * altura
totaldetinta = total / 2
print('A sua parede tem {}m²({}x{}), para pinta-la será necessário {} litros de tinta'. format(total, largura, altura, totaldetinta))