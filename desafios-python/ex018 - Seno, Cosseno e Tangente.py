import math

angulo = float(input('Digite um ângulo em graus: '))
anguloradians = math.radians(angulo)

seno = math.sin(anguloradians)
cosseno = math.cos(anguloradians)
tangente = math.tan(anguloradians)

print(f'Seno: {seno:.2f}')
print(f'Cosseno: {cosseno:.2f}')
print(f'tangente: {tangente:.2f}')