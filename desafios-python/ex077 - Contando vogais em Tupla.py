palavras = ('pastel', 'sabonete', 'panela', 'piada', 'pernambuco',
            'cachorro', 'tabuada', 'paraguai', 'esquecido')

for p in palavras:
    print(f'\nNa palavra {p} temos', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')