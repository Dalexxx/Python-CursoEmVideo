from random import randint
from time import sleep
print('Suas opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*11)
itens = ('pedra', 'papel', 'tesoura')
pc = randint(0,2)
print(f'O computador escolheu {itens[pc]}')
print(f'O jogador escolheu {itens[jogador]}')
print('-='*11)
pedra = 0
papel = 1
tesoura = 2
if jogador == pc:
    print('EMPATE')
elif jogador == pedra and pc == papel or jogador == papel and pc == tesoura or jogador == tesoura and pc == pedra:   
    print('COMPUTADOR VENCE')
else:
    print('JOGADOR VENCE')

