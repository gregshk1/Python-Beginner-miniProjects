soma = 0
contador = 0
for i in range(0,6):
    num = int(input('Digite um valor: '))
    contador += 1
    if num % 2 == 0:
        soma += num
print('Foram informados {} valores com soma total de {}.'.format(contador, soma))