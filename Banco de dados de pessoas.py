
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomehvelho = ''
totmulher20 = 0

for i in range(1, 5):
    print('----- {}ª PESSOA -----'.format(i))
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Sexo M/F: ')).strip().upper()
    somaidade += idade
    if i == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomehvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomehvelho = nome
    if sexo in 'Ff' and idade <= 20:
        totmulher20 =+ 1

mediaidade = somaidade / 4

print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomehvelho))
print('O número de mulheres com menos de 20 anos é {}'.format(totmulher20))
