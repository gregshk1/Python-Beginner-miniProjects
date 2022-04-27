v = float(input('Qual a velocidade do carro??'))

if v == 80:
    print('Você está no limite!')
if v > 80:
    multa = (v - 80) * 7
    print('Você está acima do limite e receberá multa de {}R$'.format(multa))
if v < 80:
    print('Dirija com cuidado e atente-se para os limites de velocidade. Evite multas!')