print('Vamos analisar quatro valores que serão inseridos por você:')


num = (int(input('Digite o primeiro valor: ')),
       int(input('Digite o segundo valor: ')),
       int(input('Digite o terceiro valor: ')),
       int(input('Digite o quarto valor: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('Não existe valor 3 nesta tupla.')
print('Os valores pares são:')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
