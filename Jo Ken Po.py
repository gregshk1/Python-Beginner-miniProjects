import random
itens = ['Pedra', 'Papel', 'Tesoura']
print('{:=^40}'.format(' JO KEN PO '))
print('''Selecione
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

ui = int(input('E aí qual vai ser? '))

pc = random.randint(0, 2)
print('-='*20)
print('O computador jogou {}'.format(itens[pc]))
print('O jogador jogou {}'.format(itens[ui]))
print('-='*20)

if pc == 0:
    if ui == 0:
        print('Empatamos')
    elif ui == 1:
        print('O jogador venceu')
    elif ui == 2:
        print('O computador venceu')
    else:
        print('Jogada inválida')
elif pc == 1:
    if ui == 0:
        print('O computador venceu')
    elif ui == 1:
        print('Empatamos')
    elif ui == 2:
        print('O jogador venceu')
    else:
        print('Jogada inválida')
elif pc == 2:
    if ui == 0:
        print('O jogador venceu')
    elif ui == 1:
        print('O computador venceu')
    elif ui == 2:
        print('Empatamos')
    else:
        print('Jogada inválida')
