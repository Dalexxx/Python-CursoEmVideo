print('Analisador de Triângulos')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print(f'Os seguimentos acima PODEM formar triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo!')
