sexo = str(input('Qual o seu sexo? '))
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, digite novamente: '))
print('Sexo {} registrado com sucesso'.format(sexo))