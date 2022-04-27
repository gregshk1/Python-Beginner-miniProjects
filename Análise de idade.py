from datetime import date
atual = date.today().year

for i in range(0, 7):
    idades = int(input('Digite a idade: '))
    if atual - idades >= 18:
        print('Essa pessoa é de maior')
    else:
        print('Essa pessoa é de menor')