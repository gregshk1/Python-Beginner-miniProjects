dias = float(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos Km rodou com o carro? '))
total = (60*dias) + (0.15 * km)
print('Você rodou {}Km por {:.0f} dias, o total a pagar pelo aluguel do carro é de:{:.2f}R$ '.format(km, dias, total))