from time import sleep
str(print('Olá, iremos calcular o seu BMI..'))
sleep(1)
p = float(input('Informe seu peso em KG: '))
a = float(input('Informe sua altura em CM sem pontos ou vírgulas: '))
print('Calculando..')
sleep(1)
imc = p/a**2

if imc >= 18.5 and imc == 25:
    print('Seu peso está ideal, seu IMC é {}'.format(imc))
elif imc >= 26 and imc == 30:
    print('Você tem sobrepeso, seu IMC é {}'.format(imc))
elif imc >= 31 and imc == 40:
    print('Você está obeso, seu IMC é {}'.format(imc))
elif imc > 40:
    print('Você está com obesidade mórbida e precisa de ajuda, seu IMC é {}'.format(imc))
elif imc <= 18.4:
    print('Você está abaixo do peso, seu IMC é {}'.format(imc))
