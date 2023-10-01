import math
angulo = float(input('Digite o ângulo que você deseja: '))

angulo_radianos = math.radians(angulo)
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')
print(f'O ângulo de{angulo} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de{angulo} tem a TANGENTE de {tangente:.2f}')
