distancia = int(input('Qual a distância da sua viajem em Km? '))
print(f'Você está prestes a começar uma viagem de {distancia}Km.')

preco = distancia * 0.45 if distancia > 200 else distancia * 0.50
print(f'E o preço da sua passagem será de R${preco:.2f}')