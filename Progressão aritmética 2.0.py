print('-----Gerador de PA-----')

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end='-> ')
        termo += razao
        cont += 1
    print('PAUSE')
    mais = int(input('Quantos termos a mais você quer mostrar? '))
print('FIM')