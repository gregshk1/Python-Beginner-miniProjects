from random import randint
from time import sleep
computador = randint(0, 5)


print('-=-'*15)
jogador = int(input('De 0 a 5, que número eu pensei? '))
print('-=-'*15)

print('Processando...')
sleep(1.5)

if jogador == computador:
    print('Você acertou.. af')
else:
    print('Você errou, mané, eu pensei no {}'.format(computador))