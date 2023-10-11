print('Gerador de PA')
print('-=' * 10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 0
while cont is not 10:
    print(f' {termo} >', end='')
    termo += razao
    cont += 1
print(' FIM')