agecount = malecount = womancount = 0
while True:
    sexo = ' '
    print('CADASTRE UMA PESSOA')
    idade = int(input('Idade: '))
    while sexo not in 'mf':
        sexo = input('Sexo: [M/F] ').strip().lower()
        if sexo in 'mM':
            malecount += 1
    if idade > 18:
        agecount += 1
    if idade < 20 and sexo in 'Ff':
        womancount += 1
    prox = input('Quer continuar? [S/N] ').lower().strip()
    if prox == 'n':
        break
print(f'O total de pessoas com mais de 18 anos: {agecount}')
print(f'Ao todo temos {malecount} homens cadastrados')
print(f'E temos {womancount} mulheres com menos de 20 anos')