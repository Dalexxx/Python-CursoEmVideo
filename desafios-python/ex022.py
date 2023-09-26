nome = input('Escreva seu nome completo: ').strip()

print('Analisando seu nome...')

print(f'Seu nome em maiúsculas é {nome.upper()}')

print(f'Seu nome em minúsculas é {nome.lower()}')

print(f'Seu nome ao todo tem {len(nome)-nome.count(" ")} letras')

separado = nome.split()
print(f'Seu primeiro nome é {separado[0]} e ele tem {len(separado[0])} letras')