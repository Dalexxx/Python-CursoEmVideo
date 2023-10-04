from random import randint
from time import sleep

pc = randint(0,5)
print('-=' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!'.upper())
print('-=' * 30)
player = int(input('Digite o número que eu pensei: '))
print('Deixe eu pensar...')
sleep(2)
if player == pc:
    print(f'PARABÉNS, VOCÊ GANHOU, EU PENSEI NO NÚMERO {pc}')
else:
    print(f'PERDEU OTÁRIO, EU PENSEI NO NÚMERO {pc} ')