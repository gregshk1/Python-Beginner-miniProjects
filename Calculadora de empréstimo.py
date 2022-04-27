from time import sleep
print('Olá, esse console irá te ajudar a verificar a disponibilidade de empréstimo para você.. \n')
sleep(1.5)

vC = float(input('Informe o valor da imóvel que deseja comprar: R$'))
sleep(1.5)

sal = float(input('Informe sua renda mensal: R$'))
sleep(1.5)

y = float(input('Informe em quantos anos deseja paga o imóvel: '))
sleep(1.5)
m = y * 12
vP = vC / m

if (vP) > (sal * 0.3):
    print('O valor mensal excede 30% do valor do seu salário. Empréstimo negado!')
else:
    print('Empréstimo concedido! O valor da parcela será de {:.2f}R$ paga em {:.0f} vezes'.format(vP, m))