'''nome = input('Qual é o seu nome? ')
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi {m:.1f}')
#if m >= 6:
#    print('PARABÉNS! sua média foi boa')
#else:
#    print('Sua média foi ruim. ESTUDE MAIS!')
print('PARABÉNS!' if m>= 6 else 'ESTUDE MAIS!')