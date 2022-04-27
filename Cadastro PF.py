from time import sleep
print('Olá, bem vindo ao cadastro de pessoas, siga as instruções..')
sleep(1.5)
sexoM = sexoF = nome = maiorIdade = menorIdade = novoc = 0
sexo = ''
while True:
    novoc = str(input('Deseja cadastrar uma nova pessoa? S/N: '))
    if novoc in 'Ss':
        nome = str(input('Insira o nome a ser cadastrado: '))
        idade = int(input('Digite a idade: '))
        print('-=-'*15)
        print(f'O nome cadastrado foi: \nNome:{nome} \nSexo: {sexo.upper()} \nIdade {idade} anos.')
        print('-=-' * 15)
        if sexo in 'Mm' and idade > 18:
            sexoM += 1
        elif sexo in 'Ff' and idade < 20:
            sexoF += 1
    elif novoc in 'Nn':
        print('FIM DO PROGRAMA')
        print(f'Foram cadastrados {sexoM} homens maiores de 18 anos e {sexoF} mulheres menores de 20 anos.')
        break