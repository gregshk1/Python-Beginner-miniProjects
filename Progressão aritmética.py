primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
nesimo = primeiro + (10 - 1) * razao
for i in range(primeiro, nesimo + razao, razao):
    print('{}'.format(i), end='-> ')
print('Fim')
