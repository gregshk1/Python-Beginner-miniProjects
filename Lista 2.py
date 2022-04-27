num = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado!')

    else:
        print('Valor duplicado, não será adicionado!')
    r = str(input('Deseja continuar? [S/N] '))

    if r != str:
        print('Só valores numéricos')

    if r in 'Nn':
        num.sort()
        print(f'Sua lista foi criada com os valores {num}')
        break