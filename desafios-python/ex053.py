frase = input('Digite uma frase: ').upper().replace(" ", "")
inverso = frase[::-1]
print(f'O invero de {frase} é {inverso}')
if inverso == frase:
    print('A frase digitada é um palíndromo')
else:
    print('A frase digitada não é um palíndromo')

