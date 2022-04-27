preco = float(input('Digite o valor do produto que quer calcular o desconto: '))
desconto = float(input('Agora digite o valor do desconto em porcentagem: %'))
preco2 = (preco*(desconto/100))
preco3 = preco - preco2
print('O preço original é {}, com o desconto de {}% o seu novo preço é de {}'.format(preco, desconto, preco3))