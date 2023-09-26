distancia = float(input('Qual é a distância da sua viagem? '))

print(f'Você está prestes a começar uma viagem de {distancia:.0f}Km')

if distancia <= 200:
    print(f'O preço da sua passagem será de R${distancia * 0.50:.2f}')
else:
    print(f'O preço da sua passagem será de R${distancia * 0.45:.2f}')

#preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
#print(f'E o preço da sua passagem será de R${preco:.2f}')
