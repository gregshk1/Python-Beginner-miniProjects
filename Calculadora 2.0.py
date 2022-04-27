print('-=-'*20)
print('---Olá, bem vindo a sua calculadora pessoal---')
print('---Digite dois valores e seleciona uma das opções..---')
print('-=-'*20)

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        n3 = (n1 + n2)
        print('A soma de {} e {} é {}'.format(n1, n2, n3))
    elif opcao == 2:
        n3 = (n1 * n2)
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n3))
    elif opcao == 3:
        if n1 > n2:
            print('{} > {}'.format(n1, n2))
        elif n2 > n1:
            print('{} > {}'.format(n2, n1))
        elif n1 == n2:
            print('{} = {}'.format(n1, n2))
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    print('Fechando programa')
