from random import randint
from time import sleep

cont = 0

while True:
    jogador = int(input('Digite um número de 1 a 5: '))
    sleep(1)
    print('Agora o computador irá selecionar um número..')
    computador = randint(1, 1)
    sleep(1)
    resultado1 = jogador + computador
    resultado2 = resultado1 % 2
    poui = int(input('Você quer 1 (ÍMPAR) ou 2 (PAR) '))
    if poui == 1 and resultado2 == 1:
        print(f'Você selecionou {poui} e venceu com o número {jogador}!')
        cont += 1
    elif poui == 2 and resultado2 == 0:
        print(f'Você selecionou {poui} e venceu com o número {jogador}!')
        cont += 1
    elif poui == 1 and resultado2 != 1:
        (print(f'Você perdeu e teve {cont} vitórias consecutivas.'))
        break
    elif poui == 2 and resultado != 0:
        (print(f'Você perdeu e teve {cont} vitórias consecutivas.'))
        break
print('FIM DO PROGRAMA')