nPorExtenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
               'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
               'quartorze', 'quinze', 'dessezeis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

cont = str(input('Deseja digitar um número? S/N: ')).strip().upper()


while True:
    while cont in 'Ss':
        n = int(input('Digite um número de 0 até 20 para escrevê-lo por extenso: '))
        if 0 <= n <= 20:
            print(f'Você digitou o número {nPorExtenso[n]}')
        else:
            print('O número é apenas de 0 até 20, tente novamente: ')
    if cont in 'Nn':
        print('Fim do programa')
        break