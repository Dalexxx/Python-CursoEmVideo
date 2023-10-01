velocidade = int(input('Qual é a velocidade atual do carro? '))

if velocidade > 80:
    print(f'MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você deve pagar uma multa de R${(velocidade - 80)*7}!')
else:
    print(f'Tenha um bom dia! Diriga com segurança!')