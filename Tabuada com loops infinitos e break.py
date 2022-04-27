print('-----Vamos fazer a tabuada-----')


while True:
    x = int(input('DIGITE O NÚMERO QUAL DESEJA SABER A TABUADA OU 0 PARA FECHAR O PROGRAMA:  '))
    if x == 0:
        print('FIM DO PROGRAMA')
        break
    for i in range(1, 11):
        tabuada = i * x
        print(f'A tabuada de {x} x {i} = {tabuada}')
