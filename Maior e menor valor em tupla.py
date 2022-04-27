from random import randint

gerandoTupla = int(input('''\nDeseja iniciar o programa?\n1 - SIM\n2 - NÃO: \n'''))

while True:
    if gerandoTupla == 1:
        tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
        print(f'Os números sorteados foram: {tupla} e o maior valor é de {max(tupla)} ')
        gerandoTupla = int(input('''\nDeseja gerar outra tupla?\n1 - SIM\n2 - NÃO: \n'''))
    elif gerandoTupla == 2:
        print('FIM DO PROGRAMA')
        break