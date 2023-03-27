from time import sleep
print('='*20)
print('Em uma Br onde a velocidade permitida é 80km/h...')
print('='*20)
V = int(input('Qual a Velocidade do seu carro: '))
if V > 80:
    print('Você ultrapassou o limite máximo de 80 km/h, vc foi MULTADO!')
    print('CALCULANDO SUA MULTA...')
    sleep(3)
    multa = (V - 80) * 7
    print('Sua multa vai custar R${}'.format(multa))
else:
    print('Limite permitido, tenha um bom dia!')
