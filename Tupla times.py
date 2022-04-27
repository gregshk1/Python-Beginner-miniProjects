times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preto',
         'Atlético-GO')

print('TABELA DE TIMES')

while True:
    opcao = int(input('''
    1 - MOSTRA OS CINCO PRIMEIROS TIMES
    2 - MOSTRA OS QUATRO ÚLTIMOS COLOCADOS
    3 - MOSTRA A LISTA EM ORDEM ALFABÉTICA
    4 - A POSIÇÃO DE UM TIME EM ESPECÍFICO
    5 - FECHAR O PROGRAMA
    QUAL OPÇÃO DESEJA?? '''))
    if opcao == 1:
        print(f'\nOS CINCO PRIMEIROS TIMES SÃO {times[0:6]}')
    elif opcao == 2:
        print(f'\nOS QUATRO ÚLTIMOS COLOCADOS SÃO {times[16:21]}')
    elif opcao == 3:
        print(f'\nA LISTA DE TIMES EM ORDEM ALFABÉTICA {sorted(times)}')
    elif opcao == 4:
        posicao = int(input('\nINSIRA A POSIÇÃO QUE DESEJA DO 1 AO 20: '))
        posicao1 = posicao - 1
        print(f'\nO TIME DA POSICAO {posicao} é {times[posicao1]}')
    elif opcao == 5:
        print('\nFIM DO PROGRAMA')
        break