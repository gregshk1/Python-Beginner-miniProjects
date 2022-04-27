sal = float(input('Digite o valor salário: '))

if sal >= 1250:
    nsal = (sal * 0.1) + sal
    print('Seu salário aumentou para {:.2f}'.format(nsal))
else:
    nsal2 = (sal *0.15) + sal
    print('Seu salário aumentou para {:.2f}'.format(nsal2))