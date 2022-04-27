print('Vamos somar valor!!')

qt = 0
soma = 0


while True:
    x = float(input('Digite valores para soma: '))
    if x == 999:
        print(f'Você informou {qt} valores e a soma foi de {soma}.')
        print('Fim do programa')
        break
    qt += 1
    soma += x
