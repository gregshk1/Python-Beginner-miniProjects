salario = float(input('Digite seu salário atual:R$'))
aumento = float(input('Digite em porcentagem quanto de aumento irá ganhar:%'))
salario2 = (salario*(aumento/100)) + salario
print('Com o aumento de {:.1f}% o seu novo salário é de {:.2f}'.format(aumento, salario2))