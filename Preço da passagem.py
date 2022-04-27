dist = float(input('Digite em Km a distância que sua viagem terá,'
                   'se a distância\n for maior que 200Km pagará tarifa promocional: '))

if dist > 200:
    tarifa = (dist * 0.45)
    print('O preço da sua passagem será {:.2f}R$, promocional pois'
          '\n sua viagem passa de 200Km'.format(tarifa))
else:
    tarifa2 = (dist * 0.5)
    print('O preço da sua passagem será {:.2f}R$'.format(tarifa2))
