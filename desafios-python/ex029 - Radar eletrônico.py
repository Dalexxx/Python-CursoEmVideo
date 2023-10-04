vel = int(input('Qual é a velocidade atual do seu carro? '))
mult = (vel - 80) * 7
if vel <= 80 :
    print('Tenha um bom dia! Diriga com segurança')
else:
    print(f'MULTADO! Você excedeu o limite permitido que é de 80km/h colored')
    print(f'Você deve pagar uma multa de R${mult:.2f}')
    print('Tenha um bom dia! Diriga com segurança')