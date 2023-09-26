import random
import time
print('-=-'*20, '\nVou pensar em um número entre 0 e 5. Tente adivinhar...\n', '-=-'*20)
numero = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
time.sleep(1)
numrand = random.randint(0, 5)

if numero == numrand:
    print(f'PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {numrand} e não no {numero}!')