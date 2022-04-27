from math import factorial
print('-=-'*20)
print('---Olá, bem vindo a sua calculadora pessoal---')
print('---Digite o número para calcular seu fatorial---')
print('-=-'*20)

n1 = int(input('Digite aqui o número: '))
'''f = factorial(n1)
print('O fatorial de {} é {}'.format(n1, f))'''

c = n1
while c > 0:
    n1 = n1 * (n1 -1)
    print(n1)