sexo = input('informe seu sexo: [M/F] ').upper().strip()

while sexo != 'M' and sexo != 'F':
    sexo = input('Dados inválidos. Por favor, informe seu sexo:').upper()
print(f'Sexo {sexo} registrado com sucesso')