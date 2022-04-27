import random
computerInput = random.randint(1, 10)
print('-=-'*30)
print('Vamos jogar um jogo!\n Eu vou pensar num número de 1 a 10 e você tenta adivinhar!!')
print('-=-'*30)

acertou = False
tentativas = 0

while not acertou:
    userInput = int(input('Vamos, digite um número: '))
    tentativas += 1
    if userInput < computerInput:
        print('Mais, próximo palpite! ')
    elif userInput > computerInput:
        print('Menos, diminui esse número!')
    elif userInput == computerInput:
        print('Boa, você acertou!!')
        print('Você precisou de {} palpite(s) pra acertar'.format(tentativas))