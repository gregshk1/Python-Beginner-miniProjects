print('---Sequência de Fibonacci---')
n = int(input('Digite quantos termos quer mostrar: '))
n1 = 0
n2 = 1
mais = 10
total = 0
cont = 3

print('{} -> {}'.format(n1,n2, end=''))
while mais != 0:
    total = total + mais
    while cont <= n:
        n3 = n1 + n2
        print('-> {}'.format(n3), end='')
        n1 = n2
        n2 = n3
        cont += 1
    print('\nPAUSE')
    mais = int(input('Quantos termos a mais gostaria de visualizar: '))
print('FIM DO PROGRAMA')