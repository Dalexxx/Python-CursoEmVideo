'''import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

h = math.sqrt(co**2 + ca**2)

print(f'A hipotenusa é: {h}')'''

import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

h = math.hypot(co, ca)

print(f'A hipotenusa vai medir {h:.2f}')
