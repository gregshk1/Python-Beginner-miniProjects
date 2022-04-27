num = int(input('Digite o número qual deseja saber a tabuada: '))

for i in range(0, 11):
    tabuada = i * num
    print('{} x {} = {}'.format(num, i, tabuada))